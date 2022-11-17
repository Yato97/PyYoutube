from email.mime import application
from genericpath import isdir
from unittest.mock import patch
from colorama import Fore, Style
from os import listdir, walk
from os.path import isfile, join
import xml.etree.ElementTree as et

YELLOW = Fore.YELLOW
MAGENTA = Fore.MAGENTA
BRIGHT = Style.BRIGHT
RED = Fore.RED
GREEN = Fore.GREEN
RESET = Style.RESET_ALL
CYAN = Fore.CYAN

list_repo = []
def init_menu():
    print(BRIGHT + MAGENTA + "------------- PyTool -------------")
    print(BRIGHT + YELLOW + "[" +MAGENTA + "1" +YELLOW + "]" +RESET + " - Ajouter header XML recursif")
    print(BRIGHT + YELLOW + "[" +MAGENTA + "2" +YELLOW + "]" +RESET + " - TOOL2")
    print(BRIGHT + YELLOW + "[" +MAGENTA + "3" +YELLOW + "]" +RESET + " - TOOL3")
    print(BRIGHT + YELLOW + "[" +MAGENTA + "4" +YELLOW + "]" +RESET + " - TOOL4")
    print(BRIGHT + YELLOW + "[" +MAGENTA + "5" +YELLOW + "]" +RESET + " - TOOL5")
    output = input("Outil sélectionné : ")
    return output

def router(output):
    # Output to the terminal is desired.
    if output == "1":
        print("\n"+BRIGHT + CYAN + "------------- XML TOOLS RECURSIF -------------"+ RESET)
        
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
     

if __name__ == "__main__":
    selector = init_menu()   
    router(selector)