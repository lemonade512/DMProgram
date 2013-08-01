#!/usr/bin/python

# MainFrame.py

import wx
from PlayerPanel import PlayerPanel
from MonsterPanel import MonsterPanel

class MainFrame(wx.Frame):

	def __init__(self, parent, title):
		super(MainFrame, self).__init__(parent, title=title, size=(500, 500))

		self.scroll = wx.ScrolledWindow(self, -1)
		self.scroll.SetScrollbars(1,1,10,600)
		self.scroll.SetScrollRate(1,10)

		self.InitUI()
		self.Centre()
		self.Show()

	def InitUI(self):
		p = wx.Panel(self.scroll)
		nb = wx.Notebook(p)

		ppanel = PlayerPanel(nb)
		mpanel = MonsterPanel(nb)

		nb.AddPage(ppanel, "Players")
		nb.AddPage(mpanel, "Monsters")

		sizer = wx.BoxSizer(wx.HORIZONTAL)
		sizer2 = wx.BoxSizer(wx.HORIZONTAL)
		sizer2.Add(nb,1,wx.EXPAND)
		sizer.Add(p, 1, wx.EXPAND)
		p.SetSizer(sizer2)
		self.scroll.SetSizer(sizer)

		self.Maximize()

def main():
    app = wx.App()
    MainFrame(None, "Main Frame")
    app.MainLoop()
