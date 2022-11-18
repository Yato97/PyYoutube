from email.mime import application
from genericpath import isdir
import sys
from unittest.mock import patch
from colorama import Fore, Style
from os import listdir, walk
from os.path import isfile, join
import xml.etree.ElementTree as et
from pytube import YouTube, Playlist
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

filesize = None

list_repo = []
def init_menu():
    print(BRIGHT + MAGENTA + "------------- PyTool -------------")
    print(BRIGHT + YELLOW + "[" +MAGENTA + "1" +YELLOW + "]" +RESET + " - Youtube Tools")
    print(BRIGHT + YELLOW + "[" +MAGENTA + "2" +YELLOW + "]" +RESET + " - TOOL2")
    print(BRIGHT + YELLOW + "[" +MAGENTA + "3" +YELLOW + "]" +RESET + " - TOOL3")
    print(BRIGHT + YELLOW + "[" +MAGENTA + "4" +YELLOW + "]" +RESET + " - TOOL4")
    print(BRIGHT + YELLOW + "[" +MAGENTA + "5" +YELLOW + "]" +RESET + " - TOOL5")
    output = input("Outil sélectionné : ")
    return output

def router(output):
    # Output to the terminal is desired.
    if output == "1":
        print("\n"+BRIGHT + CYAN + "------------- YOUTUBE TOOLS -------------"+ RESET)
        print(BRIGHT + YELLOW + "[" +CYAN + "1" +YELLOW + "]" +RESET + " - Avaible version")
        print(BRIGHT + YELLOW + "[" +CYAN + "2" +YELLOW + "]" +RESET + " - Download music only")
        print(BRIGHT + YELLOW + "[" +CYAN + "3" +YELLOW + "]" +RESET + " - Download video best quality")
        print(BRIGHT + YELLOW + "[" +CYAN + "4" +YELLOW + "]" +RESET + " - Download video by ITAG")
        print(BRIGHT + YELLOW + "[" +CYAN + "5" +YELLOW + "]" +RESET + " - Download playlist music only")
        outputB = input("Outil sélectionné : ")

        if outputB == "1":
            yt = selectVid(False)
            for i in yt.streams:
                print(BRIGHT + YELLOW + "[" +GREEN + "+" +YELLOW + "]" +RESET + " ",i)
                
        if outputB == "2":
            yt, tempdir= selectVid(True) 
            ys = yt.streams.get_audio_only()
            filesize = ys.filesize
            ys.download(tempdir)
            print_res_complete()
        if outputB == "3":
            yt, tempdir= selectVid(True) 
            ys = yt.streams.get_highest_resolution()
            ys.download(tempdir)
            print_res_complete()

        if outputB == "4":
            yt, tempdir= selectVid(True) 
            itag = input(BRIGHT + YELLOW + "[" +RED + "i" +YELLOW + "]" +RESET + " - ITAG : ")
            ys = yt.streams.get_by_itag(itag)
            ys.download(tempdir)
            print_res_complete()
        
        if outputB == "5":
            yt = selectPlaylist(False)
            for i in yt.length:
                print(BRIGHT + YELLOW + "[" +GREEN + "+" +YELLOW + "]" +RESET + " ",i)
                
            
            
            
        
        
    if output == "2":
        print("\n"+BRIGHT + CYAN + "------------- FILE RESEARCHER -------------"+ RESET)
                
    if output == "3":
        print("\n"+BRIGHT + CYAN + "------------- XML PARSEUR -------------"+ RESET)
            
    if output == "4":
        print("\n"+BRIGHT + CYAN + "------------- XML ANALYSEUR -------------"+ RESET)
        monRepertoire = input("Path du fichier XML : ")

    if output == "5":
        print("\n"+BRIGHT + CYAN + "------------- XML ANALYSEUR RECURSIF -------------"+ RESET)
        monRepertoire = input("Path repertoire a analyser : ")
        
def selectVid(bool):
    link = input(BRIGHT + YELLOW + "[" +RED + "/" +YELLOW + "]" +RESET + " - Link : ")
    try:
        yt = YouTube(link, on_progress_callback=progress_function)
        if(bool == True):
            root = tkinter.Tk()
            root.withdraw() #use to hide tkinter window
            currdir = os.getcwd()
            tempdir = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory to save')
            return yt, tempdir
        print(BRIGHT + YELLOW + "[" +GREEN + "+" +YELLOW + "]" +RESET + " - Connected")
        print(BRIGHT + YELLOW + "[" +MAGENTA + "*" +YELLOW + "]" +RESET + " - Download : "+yt.title)
        print(BRIGHT + YELLOW + "[" +MAGENTA + "*" +YELLOW + "]" +RESET + " - Duration : ",yt.length , "s")
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
            return yt, tempdir
        print(BRIGHT + YELLOW + "[" +GREEN + "+" +YELLOW + "]" +RESET + " - Connected")
        print(BRIGHT + YELLOW + "[" +MAGENTA + "*" +YELLOW + "]" +RESET + " - Title : "+yt.title)
        print(BRIGHT + YELLOW + "[" +MAGENTA + "*" +YELLOW + "]" +RESET + " - Number : ",yt.length)
        return yt
    except:
        print(BRIGHT + YELLOW + "[" +RED + "-" +YELLOW + "]" +RESET + " - Disconnected")
    
     
def progress_function(chunk, file_handle, bytes_remaining):
    current = ((filesize - bytes_remaining)/filesize)
    percent = ('{0:.1f}').format(current*100)
    progress = int(50*current)
    status = '█' * progress + '-' * (50 - progress)
    print(' ↳ |{bar}| {percent}%\r'.format(bar=status, percent=percent))

def print_res_complete():
    print(BRIGHT + YELLOW + "[" +CYAN + "#" +YELLOW + "]" +RESET + " - Downloading ... ")
    print(BRIGHT + YELLOW + "[" +GREEN + "+" +YELLOW + "]" +RESET + " - Done")

if __name__ == "__main__":
    selector = init_menu()   
    router(selector)