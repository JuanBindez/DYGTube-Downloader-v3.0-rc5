# this is part of the DYGtube Downloader project.
#
# Release: v2.9.1-alpha
#
# Copyright (c) 2022-2023  Juan Bindez  <juanbindez780@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#  
# repo: https://github.com/juanBindez


import os
import time

from pytube import YouTube
from pytube import Playlist
from pytube import Channel
from pytube.cli import on_progress
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from src.debug import DebugInfo
from src.progress_bar_module import progress_bar


class DownloadInit():
    """This class will receive the url to download the video."""
    def __init__(self, link_url_input):
        self.link_url_input = link_url_input

    def download_audio_mp3(self):
        """Here it will be downloaded in MP3"""
        try:
            if self.link_url_input == "":
                ask = messagebox.askokcancel("DYGTube Downloader", "The field is empty. Do you want to continue?")
                if ask == True:
                    pass
                else:
                    messagebox.showinfo("DYG Downloader", 
                                    "ok just close the mix option window!")
            elif not self.link_url_input == "":
                pass

            yt = YouTube(self.link_url_input, on_progress_callback = on_progress)
            #messagebox.showinfo("DYG Downloader", "Titulo = " + yt.title)
            ys = yt.streams.get_audio_only()
            ys.download()
            DebugInfo.logger_info.info("(From source Init) Starting to download audio MP3 from URL: %s",self.link_url_input)
            time.sleep(3)
            progress_bar()
        except KeyError:
            DebugInfo.logger_error.error(KeyError, exc_info=True)
            messagebox.showerror("DYG Downloader", "Unable to download, this is caused by some change on Youtube, try another video.")
        except Exception as e:
            DebugInfo.logger_error.error(e, exc_info=True)

        EXTENSION_MP3 = '.mp3'
        EXTENSION_MP4 = '.mp4'

        try:
            time.sleep(3)
            # renames the file with extension .mp4 to .mp3
            os.rename(str(yt.title + EXTENSION_MP4),str(yt.title + EXTENSION_MP3))
            time.sleep(1)
        except FileNotFoundError:
            messagebox.showerror("DYG Downloader", 
                                 "Error Saving With Extension .mp3!, Don't worry, just change the name of the extension manually from .mp4 to .mp3.")
        except Exception as e:
            DebugInfo.logger_error.error(e, exc_info=True)
            messagebox.showerror("DYG Downloader", 
                                 "Something went wrong!")
            pass

    def download_video_mp4(self):
        """Here it will be downloaded in MP4 video."""
        try:
            if self.link_url_input == "":
                ask = messagebox.askokcancel("DYGTube Downloader", "The field is empty. Do you want to continue?")
                if ask == True:
                    pass
                else:
                    messagebox.showinfo("DYG Downloader", 
                                    "ok just close the mix option window!")
            elif not self.link_url_input == "":
                pass

            yt = YouTube(self.link_url_input, on_progress_callback = on_progress)
            ys = yt.streams.get_highest_resolution()
            ys.download()
            DebugInfo.logger_info.info("(From source Init) Starting to download video MP4 from URL: %s",self.link_url_input)
            time.sleep(2)
            progress_bar()
        except KeyError:
            DebugInfo.logger_info.info("(Error from source Init) Error KeyError found in download video MP4 from URL: %s",self.link_url_input)
            DebugInfo.logger_error.error(KeyError, exc_info=True)
            messagebox.showerror("DYG Downloader", "Unable to download, this is caused by some change on Youtube, try another video.")
        except Exception as e:
            DebugInfo.logger_error.error(e, exc_info=True)


class PlaylistDownload():
    """Here the url of the playlist to be downloaded will be captured."""
    def __init__(self, url_playlist):    
        self.url_playlist = url_playlist

    def download_playlist_mp3(self):
        """Here the download of the playlist will start."""
        try:
            pl = Playlist(self.url_playlist)
            for video in pl.videos:
                video.streams.get_audio_only().download()
                DebugInfo.logger_info.info("(From source playlist) Starting to download audio MP3 from URL: %s",self.url_playlist)
                progress_bar()
            
                EXTENSION_MP3 = '.mp3'
                EXTENSION_MP4 = '.mp4'
                
                time.sleep(2)
                try:
                    time.sleep(2)
                    # renames the file with extension .mp4 to .mp3
                    os.rename(str(pl.title + EXTENSION_MP4),str(pl.title + EXTENSION_MP3))
                    time.sleep(1)
                    raise Exception('An error has occurred')
                except Exception as e:
                    DebugInfo.logger_error.error(e, exc_info=True)
    
                    pass
                time.sleep(1)
            raise Exception('An error has occurred')
        except FileNotFoundError:
            messagebox.showerror("DYG Downloader",
                                "If your downloads are as MP4 you will have to change to .MP3 manually, just delete the .mp4 and put .mp3.")
            DebugInfo.logger_info.info("(Error in main) exception FileNotFoundErrorfrom URL: %s",self.url_playlist)
        except Exception as e:
            error = True
            DebugInfo.logger_error.error(e, exc_info=True)
            messagebox.showerror("DYGTube Downloader",
                                 "Something went wrong! check playlist link")
        if not error:
            messagebox.showinfo("DYG Downloader", 
                                "The playlist has been downloaded successfully!")


    def download_playlist_mp4(self):
        """Here the download of the playlist will start."""
        try:
            pl = Playlist(self.url_playlist)
            for video in pl.videos:
                video.streams.get_lowest_resolution().download()
                DebugInfo.logger_info.info("(From source playlist) Starting to download video MP4 from URL: %s",self.url_playlist)
                progress_bar()
            raise Exception('An error has occurred')
        except Exception as e:
            error = True
            DebugInfo.logger_error.error(e, exc_info=True)
            messagebox.showerror("DYG Downloader", "Something went wrong! check playlist link.")
        if not error:
            messagebox.showinfo("DYG Downloader", "The playlist has been downloaded successfully!")


class ChannelDownload():
    def __init__(self, url_channel):
        self.url_channel = url_channel

    def download_channel_m4(self):
        try:
            time.sleep(3)
            c = Channel(self.url_channel)
            for video in c.videos:
                video.streams.first().download()
        except Exception as e:
            DebugInfo.logger_error.error(e, exc_info=True)
            messagebox.showerror("DYG Downloader", "Something went wrong! check channel link.")
