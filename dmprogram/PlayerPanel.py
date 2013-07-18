#!usr/bin/python

# PlayerPanel.py

import wx
import os

path, filename = os.path.split(os.path.abspath(__file__))

import utils
from Database import db
from Player import Player
from Item import Item
from NewPlayerDialog import NewPlayerDialog
from NewItemDialog import NewItemDialog
from ConfirmationDialog import ConfirmationDialog

default_text = ''

stats_string = "AC: {0}\n\
Listen: {1}\n\
Spot: {2}\n\
Search: {3}\n\
Move Silently: {4}\n\
Hide: {5}\n"

''' Panel used for creating and editing players.'''
class PlayerPanel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        self.player_list = db.LoadPlayers()

        # Init sizers
        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)

        pl_stext1 = wx.StaticText(self, label='Players')
        spacer1 = wx.StaticText(self, size=(100,3))
        pl_stext2 = wx.StaticText(self, label='Stats')
        item_stext1 = wx.StaticText(self, label='Items')
        item_stext2 = wx.StaticText(self, label='Description')

        hbox2.Add((110,-1))
        hbox2.Add(pl_stext1, 0)
        hbox2.Add((60,-1))
        hbox2.Add(pl_stext2, 0)
        hbox2.Add((235,-1))
        hbox2.Add(item_stext1, 0)
        hbox2.Add((170,-1))
        hbox2.Add(item_stext2, 0)

        # Init box that contains player and item controls and buttons
        hbox = wx.BoxSizer(wx.HORIZONTAL)

        plbtn_sizer = wx.BoxSizer(wx.VERTICAL)
        # Init button that creates new players
        new_plbtn = wx.Button(self, label='New')
        self.Bind(wx.EVT_BUTTON, self.OnNewPlayer, new_plbtn)

        # Init button that deletes selected player
        del_plbtn = wx.Button(self, label='Delete')
        self.Bind(wx.EVT_BUTTON, self.OnDelPlayer, del_plbtn)

        # Init button that edits selected player
        edit_plbtn = wx.Button(self, label='Edit')
        self.Bind(wx.EVT_BUTTON, self.OnEditPlayer, edit_plbtn)

        # Add player buttons to player button sizer
        plbtn_sizer.Add(new_plbtn, flag=wx.LEFT|wx.TOP|wx.EXPAND, border=5)
        plbtn_sizer.Add(edit_plbtn, flag=wx.LEFT|wx.TOP|wx.EXPAND, border=5)
        plbtn_sizer.Add(del_plbtn, flag=wx.LEFT|wx.TOP|wx.EXPAND, border=5)

        # Init List box for players names and bind selection event to
        # the method self.OnSelect and add it to the horizontal sizer
        self.pl_lbox = wx.ListBox(self, size=(100,300))
        for player in self.player_list:
            self.pl_lbox.Insert(player.GetName(),0)
            self.pl_lbox.SetClientData(0,player.GetID())
        self.Bind(wx.EVT_LISTBOX, self.OnPlayerSelect, self.pl_lbox)

        # Init Text Box for player stats and add it to the horizontal sizer
        self.plstats_text = wx.TextCtrl(self, size=(125, 200),
                style=wx.TE_READONLY|wx.TE_MULTILINE)

        # Init sizer for item buttons
        itembtn_sizer = wx.BoxSizer(wx.VERTICAL)
        # Init button to add an item to selected player
        new_itembtn = wx.Button(self, label='New')
        self.Bind(wx.EVT_BUTTON, self.OnNewItem, new_itembtn)
        # Init button to edit an item
        edit_itembtn = wx.Button(self, label='Edit')
        self.Bind(wx.EVT_BUTTON, self.OnEditItem, edit_itembtn)
        # Init button to delete an item
        del_itembtn = wx.Button(self, label='Delete')
        self.Bind(wx.EVT_BUTTON, self.OnDelItem, del_itembtn)
        # Add buttons to item button sizer
        itembtn_sizer.Add(new_itembtn, flag=wx.TOP, border=5)
        itembtn_sizer.Add(edit_itembtn, flag=wx.TOP, border=5)
        itembtn_sizer.Add(del_itembtn, flag=wx.TOP, border=5)

        # Init item lbox
        self.item_lbox = wx.ListBox(self, size=(200,300))
        self.Bind(wx.EVT_LISTBOX, self.OnItemSelect, self.item_lbox)

        # Init text control to display item descriptions
        self.item_text = wx.TextCtrl(self, size=(300, 200),
                style=wx.TE_READONLY|wx.TE_MULTILINE)

        line = wx.StaticLine(self, style=wx.LI_VERTICAL)

        hbox.Add(plbtn_sizer, 0, wx.ALL|wx.EXPAND, border=5)
        hbox.Add(self.pl_lbox, proportion=0, flag=wx.ALL|wx.EXPAND, border=5)
        hbox.Add(self.plstats_text, 0, flag=wx.ALL|wx.EXPAND, border=5)
        hbox.Add(line, 0, flag=wx.ALL|wx.EXPAND, border=20)
        hbox.Add(itembtn_sizer, 0, flag=wx.ALL|wx.EXPAND, border=5)
        hbox.Add(self.item_lbox, 0, flag=wx.ALL|wx.EXPAND, border=5)
        hbox.Add(self.item_text, 1, wx.ALL|wx.EXPAND, border=5)

        line2 = wx.StaticLine(self, style=wx.LI_HORIZONTAL)

        backstory_header = wx.StaticText(self, label='Backstory')

        # Init Backstory textctrl
        bstory_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.bstory_tctrl = wx.TextCtrl(self, size=(-1,400),
                                        style=wx.TE_READONLY|wx.TE_MULTILINE)

        bstory_sizer.Add(self.bstory_tctrl, 1, wx.EXPAND, border=5)

        # Add everything to main sizer
        vbox.Add(hbox2, 0, wx.TOP|wx.EXPAND, border=5)
        vbox.Add(hbox, proportion=0, flag=wx.LEFT|wx.RIGHT|wx.EXPAND,
                 border=5)
        vbox.Add(line2, 0, flag=wx.TOP|wx.LEFT|wx.RIGHT|wx.EXPAND, border=3)
        vbox.Add(backstory_header, flag=wx.ALL,border=5)
        vbox.Add(bstory_sizer, 0, wx.LEFT|wx.RIGHT|wx.EXPAND, border=5)

        self.SetSizer(vbox)

    def UpdateItemLbox(self, items):
        self.item_lbox.Clear()
        for item in items:
            self.item_lbox.Append(item.GetName(), item.GetID())

    ''' Method that runs when item in self.pl_lbox is selected '''
    def OnPlayerSelect(self, e):
        index = e.GetSelection()
        if index==wx.NOT_FOUND:
            return

        player = self.GetSelectedPlayer()
        if player == None:
            print "PlayerPanel -> OnPlayerSelect: player == None"

        else:
            stats = player.GetStats()
            value = stats_string.format(stats['AC'], stats['Listen'], 
                    stats['Spot'], stats['Search'], stats['Move_Silently'],
                    stats['Hide'])
            self.plstats_text.SetValue(value)

            items = player.GetItems()
            self.UpdateItemLbox(items)

            bstory_filename = path+'/../backstories/'+player.GetName()+'.txt'
            if os.path.isfile(bstory_filename):
                bstory_text = utils.readData(bstory_filename)
                self.bstory_tctrl.SetValue(bstory_text)
            else:
                self.bstory_tctrl.Clear()

    ''' Method that runs when new player button is hit '''
    def OnNewPlayer(self, e):
        newpl = NewPlayerDialog(None, title='New Player')
        ret = newpl.ShowModal()
        if(ret == wx.ID_OK):
            stats_dict = newpl.output
            new_player = db.CreateNewPlayer(stats_dict)
            self.player_list.append(new_player)
            self.pl_lbox.Insert(new_player.GetName(),0)
            self.pl_lbox.SetClientData(0,new_player.GetID())
        newpl.Destroy()

    ''' Method that runs when delete player button is hit '''
    def OnDelPlayer(self, e):
        condel = ConfirmationDialog(None, title='Confirm Delete',
                text = 'Are you sure you want to delete this player?')
        ret = condel.ShowModal()
        if(ret == wx.ID_OK):
            sel = self.pl_lbox.GetSelection()
            player = self.GetSelectedPlayer()
            db.DeletePlayer(player)
            self.player_list.remove(player)
            self.pl_lbox.Delete(sel)
            self.plstats_text.SetValue(default_text)
            self.item_lbox.Clear()
        condel.Destroy()

    def OnEditPlayer(self, e):
        sel = self.pl_lbox.GetSelection()
        player = self.GetSelectedPlayer()
        stats = player.GetStats()
        eplayer=NewPlayerDialog(None, 'Edit Player', stats)
        ret = eplayer.ShowModal()
        if ret == wx.ID_OK:
            stats = eplayer.output
            player = player.SetStats(**stats)
            db.SavePlayer(player)
            self.pl_lbox.Delete(sel)
            self.pl_lbox.Insert(player.GetName(), sel)
            self.pl_lbox.SetClientData(sel, player.GetID())
            self.pl_lbox.SetFocus()
            self.pl_lbox.SetSelection(sel)
            selectEvent = wx.CommandEvent(wx.wxEVT_COMMAND_LISTBOX_SELECTED,
                                          self.pl_lbox.GetId())
            self.ProcessEvent(selectEvent)
        eplayer.Destroy()

    def GetSelectedPlayer(self):
        sel = self.pl_lbox.GetSelection()
        player_id = self.pl_lbox.GetClientData(sel)
        for player in self.player_list:
            if player.GetID()==player_id:
                return player

        print "PlayerPanel -> GetSelectedPlayer: No such player"

    def GetSelectedItem(self):
        sel = self.item_lbox.GetSelection()
        item_id = self.item_lbox.GetClientData(sel)
        player = self.GetSelectedPlayer()
        items = player.GetItems()
        for item in items:
            if item.GetID() == item_id:
                return item

        print "PlayerPanel -> GetSelectedItem: No such item"

    def OnItemSelect(self, e):
        index = e.GetSelection()
        if index == wx.NOT_FOUND:
            return
    
        item = self.GetSelectedItem()
        try:
            self.item_text.SetValue(item.GetDescription())
        except:
            print "PlayerPanel -> OnItemSelect: could not set text value"

    def OnNewItem(self, e):
        newi = NewItemDialog(None, title='New Item')
        ret = newi.ShowModal()
        if ret == wx.ID_OK:
            player = self.GetSelectedPlayer()
            stats = newi.output
            stats['player_id'] = player.GetID()
            item = db.CreateNewItem(stats)
            player.AddItem(item)
            self.UpdateItemLbox(player.GetItems())
        newi.Destroy()

    def OnEditItem(self, e):
        sel = self.item_lbox.GetSelection()
        item = self.GetSelectedItem()
        stats = {'Name':item.GetName(),
                 'Description':item.GetDescription()}
        eitem=NewItemDialog(None, 'Edit Item', stats)
        ret = eitem.ShowModal()
        if ret == wx.ID_OK:
            stats = eitem.output
            item = item.SetStats(**stats)
            db.SaveItem(item)
            self.item_lbox.Delete(sel)
            self.item_lbox.Insert(item.GetName(), sel)
            self.item_lbox.SetClientData(sel, item.GetID())
            self.item_lbox.SetFocus()
            self.item_lbox.SetSelection(sel)
            selectEvent = wx.CommandEvent(wx.wxEVT_COMMAND_LISTBOX_SELECTED,
                                          self.item_lbox.GetId())
            self.ProcessEvent(selectEvent)

        eitem.Destroy()

    def OnDelItem(self, e):
        sel = e.GetSelection()
        player = self.GetSelectedPlayer()
        item = self.GetSelectedItem()
        if item != None:
            condel = ConfirmationDialog(None, title='Confirm Delete',
                    text = 'Are you sure you want to delete this item?')
            ret = condel.ShowModal()
            if ret == wx.ID_OK:
                db.DeleteItem(item)
                player.RemoveItem(item)
                self.item_lbox.Delete(sel)
                self.item_text.SetValue(default_text)
                self.UpdateItemLbox(player.GetItems())
            condel.Destroy()
        else:
            print "PlayerPanel -> OnDelItem: Item not found"
