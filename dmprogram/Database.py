#!/usr/bin/python

# Database.py

import sqlite3 as lite
import sys
import os
import utils
from Player import Player
from Item import Item

#full_path = os.path.realpath(__file__)
#path = os.path.dirname(full_path)
path, filename = os.path.split(os.path.abspath(__file__))

class Database():

    def __init__(self, name):
        self.con = lite.connect(name)
        with self.con:
            cur = self.con.cursor()
            print "Database",name,"loaded"
            sql = utils.readData(path+"/sqlScripts/player_save.sql")
            cur.executescript(sql)


    def SavePlayers(self, player_list):
        for p in player_list:
            self.SavePlayer(p)

    def SavePlayer(self, player):
        with self.con:
            cur = self.con.cursor()

            stats = ((player.GetID(), player.GetName(), player.stats['AC'],
                      player.stats['Listen'], player.stats['Spot'],
                      player.stats['Search'], player.stats['Move_Silently'],
                      player.stats['Hide']))
            cur.execute("DELETE FROM Player_Owned_Items\
                         WHERE player_id=(?)", [(player.GetID())])
            cur.execute("DELETE FROM Players WHERE player_id=(?)",
                         [(player.GetID())])
            cur.execute("INSERT INTO Players (player_id, Name, AC, Listen,\
                                              Spot, Search, Move_Silently,\
                                              Hide)\
                         VALUES(?,?,?,?,?,?,?,?)", stats)
            self.SaveItems(player.GetItems())

    def SaveItems(self, item_list):
        for item in item_list:
            self.SaveItem(item)

    def SaveItem(self, item):
        with self.con:
            cur = self.con.cursor()

            cur.execute("DELETE FROM Player_Owned_Items\
                         WHERE item_id=(?)", [(item.GetID())])
            cur.execute("INSERT INTO Player_Owned_Items\
                         (item_id, player_id, Name, Description)\
                         VALUES(?,?,?,?)", ((item.GetID(), item.GetPlayerID(),
                                             item.GetName(),
                                             item.GetDescription())))

    def LoadPlayers(self):
        player_list = []
        with self.con:
            cur = self.con.cursor()

            try:
                cur.execute("SELECT player_id FROM Players")
                rows = cur.fetchall()
                for row in rows:
                    player_id = row[0]
                    player = self.LoadPlayer(player_id)
                    player_list.append(player)
            except Exception,e:
                print "Database.py -> Database.LoadPlayers() exception"
                print str(e)
                pass

        return player_list

    def LoadPlayer(self, player_id):
        loaded_player = None
        with self.con:
            cur = self.con.cursor()

            cur.execute("SELECT * FROM Players\
                         WHERE player_id=(?)", [player_id])
            row = cur.fetchone()
            loaded_player = Player(*row)

            cur.execute("SELECT * FROM Player_Owned_Items\
                         WHERE player_id=(?)",[player_id])
            rows = cur.fetchall()
            for row in rows:
                item = Item(*row)
                loaded_player.AddItem(item)

        return loaded_player

    def DeletePlayer(self, player):
        player_id = player.GetID()
        with self.con:
            cur = self.con.cursor()
            cur.execute("DELETE FROM Player_Owned_Items\
                         WHERE player_id=(?)",[player_id])
            cur.execute("DELETE FROM Players\
                         WHERE player_id=(?)",[player_id])

    def DeleteItem(self, item):
        item_id = item.GetID()
        with self.con:
            cur = self.con.cursor()
            cur.execute("DELETE FROM Player_Owned_Items\
                         WHERE item_id=(?)",[item_id])

    def CreateNewPlayer(self, stats_dict):
        sd = stats_dict
        new_player = None
        with self.con:
            cur = self.con.cursor()

            cur.execute("INSERT INTO Players VALUES(Null,?,?,?,?,?,?,?)",
                    [sd['Name'],sd['AC'],sd['Listen'],sd['Spot'],sd['Search'],
                      sd['Move_Silently'],sd['Hide']])
            player_id = cur.lastrowid
            new_player = Player(player_id, **stats_dict)

        return new_player

    def CreateNewItem(self, stats_dict):
        sd = stats_dict
        new_item = None
        with self.con:
            cur = self.con.cursor()
            
            cur.execute("INSERT INTO Player_Owned_Items VALUES(Null,?,?,?)",
                        [sd['player_id'],sd['Name'],sd['Description']])
            item_id = cur.lastrowid
            new_item = Item(item_id, **stats_dict)

        return new_item
