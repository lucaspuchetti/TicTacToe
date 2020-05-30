#!/usr/bin/env python

class Player:
    def __init__(self, name : str , symbol : str):
        self.name = name
        self.symbol = symbol
        self.slots = set()

    def pick(self, slot : int):
        self.slots.add(slot)