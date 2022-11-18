from email.mime import application
from genericpath import isdir
import sys
from unittest.mock import patch
from colorama import Fore, Style
from os import listdir, walk
from os.path import isfile, join
import xml.etree.ElementTree as et
from pytube import YouTube, Playlist
from pytube.cli import on_progress
import tkinter
from tkinter import filedialog
import os

YELLOW = Fore.YELLOW
MAGENTA = Fore.MAGENTA
BRIGHT = Style.BRIGHT
RED = Fore.RED
GREEN = Fore.GREEN
RESET = Style.RESET_ALL
CYAN = Fore.CYAN

list_repo = []
def init_menu():
    print("\n"+BRIGHT + CYAN + "------------- YOUTUBE PYTHON TOOLS -------------"+ RESET) 
    print(BRIGHT + YELLOW + "[" +CYAN + "1" +YELLOW + "]" +RESET + " - Avaible version")
    print(BRIGHT + YELLOW + "[" +CYAN + "2" +YELLOW + "]" +RESET + " - Download music only")
    print(BRIGHT + YELLOW + "[" +CYAN + "3" +YELLOW + "]" +RESET + " - Download video best quality")
    print(BRIGHT + YELLOW + "[" +CYAN + "4" +YELLOW + "]" +RESET + " - Download video by ITAG")
    print(BRIGHT + YELLOW + "[" +CYAN + "5" +YELLOW + "]" +RESET + " - Parse playlist")
    print(BRIGHT + YELLOW + "[" +CYAN + "6" +YELLOW + "]" +RESET + " - Download playlist music only")
    print(BRIGHT + YELLOW + "[" +CYAN + "7" +YELLOW + "]" +RESET + " - Download playlist video")
    output = input("Outil sélectionné : ")
    return output

def router(output):
        if output == "1":
            yt = selectVid(False)
            for i in yt.streams:
                print(BRIGHT + YELLOW + "[" +GREEN + "+" +YELLOW + "]" +RESET + " ",i)
                
        if output == "2":
            yt, tempdir= selectVid(True) 
            ys = yt.streams.get_audio_only()
            ys.download(tempdir)
        if output == "3":
            yt, tempdir= selectVid(True) 
            ys = yt.streams.get_highest_resolution()
            ys.download(tempdir)

        if output == "4":
            yt, tempdir= selectVid(True) 
            itag = input(BRIGHT + YELLOW + "[" +RED + "i" +YELLOW + "]" +RESET + " - ITAG : ")
            ys = yt.streams.get_by_itag(itag)
            ys.download(tempdir)
        
        if output == "5":
            yt = selectPlaylist(False)
            for i in yt.videos:
                print(BRIGHT + YELLOW + "[" +GREEN + "+" +YELLOW + "]" +RESET + " ",i.title)
                print(BRIGHT + YELLOW + "[" +CYAN + "-" +YELLOW + "]" +RESET + " ",i.embed_url)
        
        if output == "6":
            yt, tempdir = selectPlaylist(True)
            for i in yt.videos:
                print(BRIGHT + YELLOW + "[" +GREEN + "+" +YELLOW + "]" +RESET + " ",i.title)
                ys = i.streams.get_audio_only()
                ys.download(tempdir)

        
        if output == "7":
            yt, tempdir = selectPlaylist(True)
            for i in yt.videos:
                print(BRIGHT + YELLOW + "[" +GREEN + "+" +YELLOW + "]" +RESET + " ",i.title)
                ys = i.streams.get_highest_resolution()
                ys.download(tempdir)
        print(BRIGHT + YELLOW + "[" +GREEN + "+" +YELLOW + "]" +RESET + " - Done")
        
def selectVid(bool):
    link = input(BRIGHT + YELLOW + "[" +RED + "/" +YELLOW + "]" +RESET + " - Link : ")
    try:
        yt = YouTube(link, on_progress_callback=progress_function)
        if(bool == True):
            root = tkinter.Tk()
            root.withdraw() #use to hide tkinter window
            currdir = os.getcwd()
            tempdir = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory to save')
            print(BRIGHT + YELLOW + "[" +GREEN + "+" +YELLOW + "]" +RESET + " - Connected")
            print(BRIGHT + YELLOW + "[" +RED + "-" +YELLOW + "]" +RESET + " - Fetching : "+yt.title)
            print(BRIGHT + YELLOW + "[" +MAGENTA + "-" +YELLOW + "]" +RESET + " - Duration : ",yt.length , "s")
            print(BRIGHT + YELLOW + "[" +CYAN + "#" +YELLOW + "]" +RESET + " - Downloading ...")
            return yt, tempdir
        print(BRIGHT + YELLOW + "[" +GREEN + "+" +YELLOW + "]" +RESET + " - Connected")
        print(BRIGHT + YELLOW + "[" +RED + "-" +YELLOW + "]" +RESET + " - Fetching : "+yt.title)
        print(BRIGHT + YELLOW + "[" +MAGENTA + "-" +YELLOW + "]" +RESET + " - Duration : ",yt.length , "s")
        return yt
    except:
        print(BRIGHT + YELLOW + "[" +RED + "-" +YELLOW + "]" +RESET + " - Disconnected")

def selectPlaylist(bool):
    link = input(BRIGHT + YELLOW + "[" +RED + "/" +YELLOW + "]" +RESET + " - Link playlist : ")
    try:
        yt = Playlist(link)
        if(bool == True):
            root = tkinter.Tk()
            root.withdraw() #use to hide tkinter window
            currdir = os.getcwd()
            tempdir = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory to save')
            print(BRIGHT + YELLOW + "[" +GREEN + "+" +YELLOW + "]" +RESET + " - Connected")
            print(BRIGHT + YELLOW + "[" +MAGENTA + "*" +YELLOW + "]" +RESET + " - Fetching : "+yt.title)
            print(BRIGHT + YELLOW + "[" +MAGENTA + "*" +YELLOW + "]" +RESET + " - Number : ",yt.length)
            print(BRIGHT + YELLOW + "[" +CYAN + "#" +YELLOW + "]" +RESET + " - Downloading ...")
            return yt, tempdir
        print(BRIGHT + YELLOW + "[" +GREEN + "+" +YELLOW + "]" +RESET + " - Connected")
        print(BRIGHT + YELLOW + "[" +MAGENTA + "*" +YELLOW + "]" +RESET + " - Title : "+yt.title)
        print(BRIGHT + YELLOW + "[" +MAGENTA + "*" +YELLOW + "]" +RESET + " - Number : ",yt.length)
        return yt
    except:
        print(BRIGHT + YELLOW + "[" +RED + "-" +YELLOW + "]" +RESET + " - Disconnected")
    
def progress_function(chunk, file_handle, bytes_remaining):
    filesize = chunk.filesize
    current = ((filesize - bytes_remaining)/filesize)
    percent = ('{0:.1f}').format(current*100)
    progress = int(50*current)
    status = '█' * progress + '-' * (50 - progress)
    sys.stdout.write(' ↳ |{bar}| {percent}%\r'.format(bar=status, percent=percent))
    sys.stdout.flush()
    print("\n")

if __name__ == "__main__":
    selector = init_menu()   
    router(selector)