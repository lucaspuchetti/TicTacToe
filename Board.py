#!/usr/bin/env python
class Board():
    def __init__(self):
        self.slots = [i for i in range(1 , 10)]
        self.keybinds = {str(i) : i for i in range(1,10)}
        self.occupiedSlots = []