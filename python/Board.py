#!/usr/bin/env python

class Board:
    """
    A borad has slots that are binded to the flattened matrix.
    Used (occupied) slots are replaced for the players' symbol.
    
    Slots handle the state of each slot, i.e. how they look.
    Keybinds handle the relation between input and the underlying
    matrix.
    occupiedSlots handle the positions already taken, to ease 
    verification of valid plays.
    The snapshot is a formatted string with the current look of 
    the board.
    """
    def __init__(self , *args):
        self.slots = list("789456123")
        self.keybinds = {str(key) : pos for pos , key \
                            in enumerate(self.slots)}
        self.occupiedSlots = []
        self.setSnapshot()
    
    def changeKeybind(self , keybindString : str):
        self.keybinds = {key : pos for pos,key in \
                            enumerate(keybindString) }
        self.resetBoard()

    def resetBoard(self):
        newSlots = sorted(self.keybinds.items() , key=lambda x: x[1])
        newSlots = [ i for i in map(lambda x: x[0] , newSlots) ]
        self.slots = newSlots
        self.occupiedSlots = [] # makes sure the game restarts
        self.setSnapshot()

    def getPosition(self,keybind):
        return self.keybinds[keybind]

    def setSnapshot(self):
        snapshot = []
        for firstInRow in range(0 , len(self.slots) , 3):
            line = "|{0}|{1}|{2}|".format(*self.slots[firstInRow : firstInRow+3 ])
            snapshot.append(line)
        else:
            self.snapshot = snapshot
    
    def getSnapshot(self):
        return self.snapshot
    
    def addChoice(self, key : str , symbol : str):
        if key not in self.keybinds.keys():
            return (False , "{} is not a valid slot.".format(key) )
        elif key not in self.occupiedSlots:
            self.occupiedSlots.append(key)
            keyPosition = self.keybinds[key]
            self.slots[keyPosition] = symbol
            self.setSnapshot()
            return (True , "{} took {}".format(symbol , key) ) 
        else:
            return (False , "{} is already occupied.".format(key) )
    

    