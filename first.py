import wx

app = wx.App()
frm = wx.Frame(None, title="Hello World!", size=(400, 300), pos=(100, 100))

frm.Show()
app.MainLoop()