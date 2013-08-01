#!/usr/bin/python

# Player.py

import sqlite3 as lite
import sys
import utils
from Item import Item

class Player():

    def __init__(self, player_id=-1, Name='', AC=-1, Listen=-1, 
                 Spot=-1, Search=-1, Move_Silently=-1, Hide=-1):
        self.stats = {"ID":int(player_id), "Name":Name, "AC":int(AC), 
                      "Listen":int(Listen), "Spot":int(Spot), 
                      "Search":int(Search), "Move_Silently":int(Move_Silently),
                      "Hide":int(Hide)}
        self.items = []

    def GetStats(self):
        return self.stats

    def GetName(self):
        return self.stats['Name']

    def GetID(self):
        return self.stats['ID']

    def GetAC(self):
        return self.stats['AC']

    def GetListen(self):
        return self.stats['Listen']

    def GetSpot(self):
        return self.stats['Spot']

    def GetSearch(self):
        return self.stats['Search']

    def GetMoveSilently(self):
        return self.stats['Move_Silently']

    def GetHide(self):
        return self.stats['Hide']

    def SetStats(self, Name, AC, Listen, Spot, Search, Move_Silently, Hide):
        pl_id = self.GetID()
        self.stats['Name'] = Name
        self.stats['AC'] = AC
        self.stats['Listen'] = Listen
        self.stats['Spot'] = Spot
        self.stats['Search'] = Search
        self.stats['Move_Silently'] = Move_Silently
        self.stats['Hide'] = Hide
        assert(self.GetID()==pl_id)
        return self

    def AddItem(self, item):
        self.items.append(item)

    def RemoveItem(self, item):
        self.items.remove(item)

    def AddItems(self, *args, **kwargs):
        for item in args:
            assert(isinstance(item,Item))
            self.AddItem(item)

    def GetItems(self):
        return self.items
