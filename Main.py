#!/usr/bin/env python

from Board import Board
from Console import Console
from Player import Player
from Game import Game
from Menu import Menu
from time import sleep

def main():
    # Main function for the game
    board , console = Board() , Console()
    console.print("Welcome to TicTacToe!")
    player1Name = console.input("Insert Player 1's name")
    player2Name = console.input("Insert Player 2's name")
    player1 = Player(player1Name , "O")
    player2 = Player(player2Name , "X")
    game = Game(player1 , player2 , board , console)
    tictactoe = Menu(game)
    tictactoe.game.resetGame()
    
    wantsToExit = False
    while not wantsToExit:
        tictactoe.print(*["What would you like to do?" ,
                         "a - Play TicTacToe!",
                         "b - Change board layout",
                         "c - Change Player's name and symbol" ,
                         "d - Exit the game"])
        command = tictactoe.input().lower()
        if command in ("a" , "play"):
            tictactoe.game.resetGame()
            tictactoe.playTicTacToe()
        elif command in ("b" , "board"):
            tictactoe.changeKeyLayout()
        elif command in ("c" , "player"):
            tictactoe.changePlayerData()
        elif command in ("d" , "exit"):
            tictactoe.print("Thanks for playing!")
            sleep(1)
            wantsToExit = True
        else:
            tictactoe.print("Wrong command.")

if __name__ == "__main__":
    main()


