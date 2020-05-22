#!/usr/bin/env python
import platform
import os

class Console:
    def __init__(self, *args):
        self.title = \
"""|_   _(_)      |_   _|          |_   _|         
  | |  _  ___    | | __ _  ___    | | ___   ___ 
  | | | |/ __|   | |/ _` |/ __|   | |/ _ \ / _ \\
  | | | | (__    | | (_| | (__    | | (_) |  __/
  \_/ |_|\___|   \_/\__,_|\___|   \_/\___/ \___|"""
        self.__setOSClear__()
    
    def __setOSClear__(self):
        if platform.system() == "Windows":
            self.clear = lambda : os.system("cls")
        else:
            self.clear = lambda : os.system("clear")
    
    def printWithTitle(self, *args , **kwargs):
        self.clear()
        print(self.title)
        print(*args , **kwargs)

    def spaceHandler(self):
        # Create a function that handles 
        # multiple lines keeping the console clean.
        pass

    