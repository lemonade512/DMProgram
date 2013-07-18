#!/usr/bin/python

from Player import Player
from Item import Item
from Database import db

new_player_stats = {
	'Name':'TestPlayer',
	'AC':5,
	'Listen':3,
	'Spot':4,
	'Search':2,
	'Move_Silently':2,
	'Hide':4
}

new_player = db.CreateNewPlayer(new_player_stats)

print new_player.stats
