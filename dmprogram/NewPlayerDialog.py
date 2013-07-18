#!/usr/bin/python

# NewPlayerDialog.py

import wx

empty_stats={'Name':'',
		     'AC':'',
			 'Listen':'',
			 'Spot':'',
			 'Search':'',
			 'Move_Silently':'',
			 'Hide':''}

class NewPlayerDialog(wx.Dialog):

	def __init__(self, parent, title, stats=empty_stats, *args, **kwargs):
		super(NewPlayerDialog, self).__init__(parent, *args, **kwargs)

		self.output=stats
		self.InitUI()
		self.SetSize((250,250))
		self.SetTitle(title)

	def InitUI(self):
		pnl = wx.Panel(self)
		vbox1 = wx.BoxSizer(wx.VERTICAL)
		vbox2 = wx.BoxSizer(wx.VERTICAL)

		grid_sizer = wx.GridSizer(rows=7, cols=2, vgap=5, hgap=5)

		st1 = wx.StaticText(pnl, label='Name')
		self.tctrl1 = wx.TextCtrl(pnl, value=str(self.output['Name']))

		st2 = wx.StaticText(pnl, label='AC')
		self.tctrl2 = wx.TextCtrl(pnl, value=str(self.output['AC']))

		st3 = wx.StaticText(pnl, label='Listen')
		self.tctrl3 = wx.TextCtrl(pnl, value=str(self.output['Listen']))

		st4 = wx.StaticText(pnl, label='Spot')
		self.tctrl4 = wx.TextCtrl(pnl, value=str(self.output['Spot']))

		st5 = wx.StaticText(pnl, label='Search')
		self.tctrl5= wx.TextCtrl(pnl, value=str(self.output['Search']))

		st6 = wx.StaticText(pnl, label='Move Silently')
		self.tctrl6 = wx.TextCtrl(pnl, value=str(self.output['Move_Silently']))

		st7 = wx.StaticText(pnl, label='Hide')
		self.tctrl7 = wx.TextCtrl(pnl, value=str(self.output['Hide']))

		hbox = wx.BoxSizer(wx.HORIZONTAL)
		okbtn = wx.Button(pnl, label='Ok', size=(85,28))
		clsbtn = wx.Button(pnl, label='Close', size=(85,28))
		hbox.Add(okbtn, flag=wx.RIGHT|wx.EXPAND, border=5)
		hbox.Add(clsbtn, flag=wx.EXPAND)

		grid_sizer.AddMany( [(st1),(self.tctrl1),(st2),(self.tctrl2),
							 (st3),(self.tctrl3),(st4),(self.tctrl4),
							 (st5),(self.tctrl5),(st6),(self.tctrl6),
							 (st7),(self.tctrl7)] )

		vbox2.Add(grid_sizer, flag=wx.ALIGN_CENTER)
		vbox2.Add(hbox, flag=wx.ALIGN_CENTER|wx.TOP|wx.LEFT|wx.RIGHT, border=5)
		pnl.SetSizerAndFit(vbox2)

		vbox1.Add(pnl,proportion=1, flag=wx.EXPAND|wx.ALL, border=10)
		self.SetSizerAndFit(vbox1)

		self.Bind(wx.EVT_BUTTON, self.OnClose, clsbtn)
		self.Bind(wx.EVT_BUTTON, self.OnOk, okbtn)

		self.tctrl1.SetFocus()

	def OnClose(self, e):
		self.Destroy()

	def OnOk(self, e):
		self.output={'Name':self.tctrl1.GetValue(),
					 'AC':self.tctrl2.GetValue(),
				     'Listen':self.tctrl3.GetValue(),
					 'Spot':self.tctrl4.GetValue(),
					 'Search':self.tctrl5.GetValue(),
					 'Move_Silently':self.tctrl6.GetValue(),
					 'Hide':self.tctrl7.GetValue()}
		self.EndModal(wx.ID_OK)
