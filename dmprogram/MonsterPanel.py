#!/usr/bin/python

# MonsterPanel.py

import wx

class MonsterPanel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        stext = wx.StaticText(self, label="This is the monster panel")
