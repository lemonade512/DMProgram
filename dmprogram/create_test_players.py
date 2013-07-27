import sys

from Database import Database
db = Database('../save.db')

p1_stats = {
		'Name':'Test Player 1',
		'AC':1,
		'Listen':1,
		'Spot':1,
		'Search':1,
		'Move_Silently':1,
		'Hide':1}

p2_stats = {
		'Name':'Test Player 2',
		'AC':2,
		'Listen':2,
		'Spot':2,
		'Search':2,
		'Move_Silently':2,
		'Hide':2}

p1 = db.CreateNewPlayer(p1_stats)
p2 = db.CreateNewPlayer(p2_stats)

p1i1_stats = {'Name':'Player 1 Item 1', 'Description':'p1i1 description',
			  'player_id':p1.GetID()}
p1i2_stats = {'Name':'Player 2 Item 2', 'Description':'p1i2 description',
			  'player_id':p1.GetID()}
p1i3_stats = {'Name':'Player 2 Item 2', 'Description':'This is a copy',
			  'player_id':p1.GetID()}

p2i1_stats = {'Name':'Awesome item', 'Description':'Awesome description',
			  'player_id':p2.GetID()}

p1i1 = db.CreateNewItem(p1i1_stats)
p1i2 = db.CreateNewItem(p1i2_stats)
p1i3 = db.CreateNewItem(p1i3_stats)

p2i1 = db.CreateNewItem(p2i1_stats)

p1.AddItems(p1i1,p1i1,p1i3)
print p1.GetItems()

p2.AddItem(p2i1)
