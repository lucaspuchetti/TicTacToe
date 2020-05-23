#!/usr/bin/env python
import platform
import os

class Console:
    bufferLimit = 6
    def __init__(self, *args):
        self.title = \
"""|_   _(_)      |_   _|          |_   _|         
  | |  _  ___    | | __ _  ___    | | ___   ___ 
  | | | |/ __|   | |/ _` |/ __|   | |/ _ \ / _ \\
  | | | | (__    | | (_| | (__    | | (_) |  __/
  \_/ |_|\___|   \_/\__,_|\___|   \_/\___/ \___|"""
        self.__setOSClear__()
        self.cachedBoard = ""
        self.buffer = []
    
    def __setOSClear__(self):
        if platform.system() == "Windows":
            self.clear = lambda : os.system("cls")
        else:
            self.clear = lambda : os.system("clear")
    
    def __printWithInterface__(self):
        self.clear()
        print(self.title)
        print(self.cachedBoard)
        print("\n".join(self.buffer))

    def push(self, *args):
        self.buffer = self.buffer + list(args)
        bufferedItems = len(self.buffer)
        if bufferedItems > self.bufferLimit:
            self.buffer = self.buffer[bufferedItems-self.bufferLimit:]
        
    def input(self, message :str = None):
        if message is not None:
            self.push(message)
        self.__printWithInterface__()
        answer = input()
        self.push(answer)
        self.__printWithInterface__()
        return answer

    def print(self , *args):
        self.push(args)
        self.__printWithInterface__()

    def updateBoard(self, newBoard:str):
        self.cachedBoard = newBoard
    