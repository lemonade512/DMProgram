#!/usr/bin/python

# NewItemDialog.py

import wx

empty_stats = {'Name':'', 'Description':''}

class NewItemDialog(wx.Dialog):

    def __init__(self, parent, title, stats=empty_stats, *args, **kwargs):
        super(NewItemDialog, self).__init__(parent, *args, **kwargs)

        assert('Name' in stats)
        assert('Description' in stats)

        self.output=stats
        self.InitUI()
        self.SetSize((250,400))
        self.SetTitle(title)

    def InitUI(self):
        pnl = wx.Panel(self, style=wx.BORDER_SIMPLE)
        vbox1 = wx.BoxSizer(wx.VERTICAL)
        vbox2 = wx.BoxSizer(wx.VERTICAL)

        grid_sizer = wx.FlexGridSizer(rows=2, cols=2, vgap=5, hgap=5)

        st1 = wx.StaticText(pnl, label='Name')
        self.tctrl1 = wx.TextCtrl(pnl, value=str(self.output['Name']))

        st2 = wx.StaticText(pnl, label='Desc')
        self.tctrl2 = wx.TextCtrl(pnl, size=(150, 200), style=wx.TE_MULTILINE,
                                  value = str(self.output['Description']))

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        okbtn = wx.Button(pnl, label='Ok', size=(85,28))
        clsbtn = wx.Button(pnl, label='Close', size=(85,28))
        hbox.Add(okbtn, flag=wx.RIGHT|wx.EXPAND, border=5)
        hbox.Add(clsbtn, flag=wx.EXPAND)

        grid_sizer.AddMany( [(st1),(self.tctrl1, 1, wx.EXPAND),(st2),
                             (self.tctrl2, 1, wx.EXPAND)] )

        grid_sizer.AddGrowableRow(1,1)
        grid_sizer.AddGrowableCol(1,1)

        vbox2.Add(grid_sizer, flag=wx.ALIGN_CENTER)
        vbox2.Add(hbox, flag=wx.ALIGN_CENTER|wx.TOP|wx.LEFT|wx.RIGHT, border=5)
        pnl.SetSizerAndFit(vbox2)

        vbox1.Add(pnl,proportion=1,flag=wx.EXPAND|wx.ALL,border=10)
        self.SetSizerAndFit(vbox1)

        self.Bind(wx.EVT_BUTTON, self.OnClose, clsbtn)
        self.Bind(wx.EVT_BUTTON, self.OnOk, okbtn)

        self.tctrl1.SetFocus()

    def OnClose(self, e):
        self.Destroy()

    def OnOk(self, e):
        self.output={'Name':self.tctrl1.GetValue(),
                     'Description':self.tctrl2.GetValue()}
        self.EndModal(wx.ID_OK)
