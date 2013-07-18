#!/usr/bin/python

# Player.py

class Item():

	def __init__(self, item_id, player_id, Name, Description):
		self.ID = item_id
		self.player_id = player_id
		self.Name = Name
		self.Description = Description

	def GetName(self):
		return self.Name

	def GetID(self):
		return self.ID

	def GetPlayerID(self):
		return self.player_id

	def GetDescription(self):
		return self.Description

	def SetStats(self, Name, Description):
		pl_id = self.GetPlayerID()
		it_id = self.GetID()
		self.Name = Name
		self.Description = Description
		assert(self.GetPlayerID()==pl_id)
		assert(self.GetID()==it_id)
		return self
