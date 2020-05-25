#!/usr/bin/env python

from Board import Board
from Console import Console
from Player import Player
from Game import Game

class Menu:

    def __init__(self, game: Game):
        self.game = game

    def changeKeyLayout(self):
        successfull = False
        bannedLetters = self.game.players["p1"].symbol +\
                        self.game.players["p2"].symbol
        while not successfull:
            msg = ["Please, enter the keys you want to use for the game from left to right, and top to bottom" , 
                   "For example, to play with a numeric pad, you'd enter 789456123",
                   'To exit without making changes, enter "exit"']
            self.print(*msg)
            newKeybinds = self.input()
            if newKeybinds == "exit":
                return
            elif bannedLetters[0] in newKeybinds or \
                 bannedLetters[1] in newKeybinds:
                self.game.console.purge()
                self.print("You cannot use letters that are used as players' symbols.")            
            elif len(set(newKeybinds)) == len(newKeybinds) and len(newKeybinds) == 9:
                successfull = True
                self.game.resetGame()
                self.game.board.changeKeybind(newKeybinds)
                self.game.console.updateBoard(self.game.board.getSnapshot())
                self.print("Update successful!")
            else:
                self.game.console.purge()
                self.print("Process failed, try again.")
    
    def changePlayerData(self):
        successfull = False
        while not successfull:
            playerKey = self.input(
                    'Enter p1 to change Player 1 data, or p2 to change Player 2 data. Enter "exit" to go back.')
            if playerKey == "exit":
                return
            elif playerKey in ("p1" , "p2"):
                successfull = True
            else:
                self.print("Incorrect option.")
        
        newName = self.input("Enter your new name. Press enter to skip.")
        if newName != "":
            self.game.players[playerKey].name = newName
        
        newSymbol = self.input("Enter your new symbol. Press enter to skip.")
        if newSymbol != "":
            self.game.players[playerKey].symbol = newSymbol[0]
        
    
        self.print("Changes saved successfully.")

    def playTicTacToe(self):
        keepPlaying = True
        while keepPlaying:
            self.print("Let's get started!")
            self.game.playGame()
            replay = self.input("Rematch?")
            if replay.lower() in ("y" , "yes"):
                self.game.resetGame()
                continue
            else:
                keepPlaying = False
    
    def print(self, *args):
        self.game.console.print(*args)
    
    def input(self, *args):
        return self.game.console.input(*args)