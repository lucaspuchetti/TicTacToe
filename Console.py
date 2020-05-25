#!/usr/bin/env python

import platform
import os

class Console:
    bufferLimit = 6
    title = \
""" _______        ______           ______ 
|_   _(_)      |_   _|          |_   _|         
  | |  _  ___    | | __ _  ___    | | ___   ___ 
  | | | |/ __|   | |/ _` |/ __|   | |/ _ \ / _ \\
  | | | | (__    | | (_| | (__    | | (_) |  __/
  \_/ |_|\___|   \_/\__,_|\___|   \_/\___/ \___|"""
    
    def __init__(self, *args):
        self.__setOSClear__()
        self.cachedBoard = ""
        self.buffer = []
        self.setPadding()
    
    def __setOSClear__(self):
        if platform.system() == "Windows":
            self.clear = lambda : os.system("cls")
        else:
            self.clear = lambda : os.system("clear")
    
    def __printWithInterface__(self):
        self.clear()
        print(self.title , "\n")
        print(self.cachedBoard , "\n")
        print("\n".join(self.buffer))

    def push(self, *args):
        self.buffer = self.buffer + list(args)
        bufferLength = len(self.buffer)
        if bufferLength > self.bufferLimit:
            self.buffer = self.buffer[bufferLength-self.bufferLimit:]

    def purge(self, purgeBoard : bool = False):
        if purgeBoard:
            self.cachedBoard = ""
        self.buffer = []
           
    def input(self, message :str = None):
        if message is not None:
            self.push(message)
        self.__printWithInterface__()
        answer = input()
        self.push(answer)
        self.__printWithInterface__()
        return answer

    def print(self , *args):
        self.push(*args)
        self.__printWithInterface__()

    def updateBoard(self, newBoard:list):
        boardLines = [self.padding + i + self.padding for i in newBoard]
        self.cachedBoard = "\n".join(boardLines)
    
    def setPadding(self):
        titleLines = self.title.split("\n")
        maxLength = max([ len(i) for i in titleLines])
        rawPadding = ( maxLength - 7 ) / 2
        self.padding = " " * int(rawPadding//1)