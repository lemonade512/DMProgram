#!/usr/bin/python

# ConfirmationDialog.py

import wx

class ConfirmationDialog(wx.Dialog):

	def __init__(self, parent, title, text, *args, **kwargs):
		super(ConfirmationDialog, self).__init__(parent, *args, **kwargs)

		self.InitUI(text)
		self.SetSize((400,100))
		self.SetTitle(title)

	def InitUI(self, text):
		pnl = wx.Panel(self)
		vbox1 = wx.BoxSizer(wx.VERTICAL)
		vbox2 = wx.BoxSizer(wx.VERTICAL)

		st = wx.StaticText(pnl, label=text)

		btn_sizer = wx.BoxSizer(wx.HORIZONTAL)
		ybtn = wx.Button(pnl, label='Yes', size=(85,28))
		self.Bind(wx.EVT_BUTTON, self.OnYes, ybtn)
		nbtn = wx.Button(pnl, label='No', size=(85,28))
		self.Bind(wx.EVT_BUTTON, self.OnNo, nbtn)
		btn_sizer.Add(ybtn, 0, wx.EXPAND|wx.ALIGN_CENTER|wx.ALL, border=5)
		btn_sizer.Add(nbtn, 0, wx.EXPAND|wx.ALIGN_CENTER|wx.ALL, border=5)

		vbox2.Add(st, 0, wx.ALIGN_CENTER|wx.ALL, border=5)
		vbox2.Add(btn_sizer, 0, wx.ALIGN_CENTER|wx.ALL, border=5)

		pnl.SetSizerAndFit(vbox2)

		vbox1.Add(pnl, 1, flag=wx.EXPAND|wx.ALL, border=10)
		self.SetSizerAndFit(vbox1)

	def OnNo(self, e):
		self.Destroy()

	def OnYes(self, e):
		self.EndModal(wx.ID_OK)
