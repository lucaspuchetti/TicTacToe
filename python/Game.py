#!/usr/bin/env python

from Board import Board
from Console import Console
from Player import Player

class Game:

    winningSets = [
        {0 , 1 , 2},
        {3 , 4 , 5},
        {6 , 7 , 8},
        {0 , 3 , 6},
        {1 , 4 , 7},
        {2 , 5 , 8},
        {0 , 4 , 8},
        {2 , 4 , 6}        
    ]

    def __init__(self,  player1 : Player, 
                        player2 : Player, 
                        board : Board,
                        console : Console):
        self.players = { "p1" : player1,
                         "p2" : player2
        }
        self.board = board
        self.console = console
        self.winner = None
    
    def checkWinner(self , playerKey : str):
        playerSlots = self.players[playerKey].slots
        for winCondition in self.winningSets:
            if winCondition.issubset(playerSlots):
                self.winner = self.players[playerKey]
                return True
        return False
    
    def checkEndOfGame(self):
        # Checks end of the game and winner
        haveWinner = False
        for player in self.players.keys():
            haveWinner = self.checkWinner(player)
            if haveWinner:
                return (True , True)
        if len(self.board.occupiedSlots) == 9:
            return (True , False)
        else:
            return (False , False)
        


    def turn(self , playerKey : str):
        playerSymbol = self.players[playerKey].symbol
        succesfulTurn , msg = False , ""
        while not succesfulTurn:
            playerMove = self.console.input("Please make a move, {}".\
                            format(self.players[playerKey].name))
            succesfulTurn , msg = self.board.\
                                    addChoice(playerMove , playerSymbol)
            self.console.print(msg)
            if succesfulTurn:
                self.players[playerKey].\
                    pick(self.board.getPosition(playerMove))
                self.console.updateBoard(self.board.getSnapshot())

    def round(self):
        for player in self.players.keys():
            self.turn(player)
            finishedGame , haveWinner = self.checkEndOfGame()
            if finishedGame:
                return (finishedGame , haveWinner)
        else:
            return (finishedGame , haveWinner)
    
    def playGame(self):
        finishedGame , haveWinner = False , False
        while not finishedGame:
            finishedGame , haveWinner = self.round()
        if haveWinner:
            self.console.print("Cogratulations {}! You win!".\
                                    format(self.winner.name))
        else:
            self.console.print("It's a tie!")

    def resetGame(self):
        self.winner = None
        for playerKey in self.players.keys():
            self.players[playerKey].slots = set()
        self.board.resetBoard()
        self.console.purge(purgeBoard = True)
        self.console.updateBoard(self.board.getSnapshot())
        
