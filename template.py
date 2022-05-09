import wx

class myFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="muban", size=(500, 600), pos=(200, 200))


class App(wx.App):

    def OnInit(self):
        frame = myFrame()
        frame.Show()
        return True

    def OnExit(self):
        return 0

if __name__ == '__main__':
    app = App()
    app.MainLoop()
