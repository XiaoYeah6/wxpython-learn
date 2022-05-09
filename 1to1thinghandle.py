from cProfile import label
import wx

class myFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="muban", size=(500, 600), pos=(200, 200))
        self.Centre()
        panel = wx.Panel(parent=self)
        self.statictext = wx.StaticText(parent=panel, pos=(110, 20))
        b = wx.Button(parent=panel, label='ok', pos=(100, 50))
        self.Bind(wx.EVT_BUTTON, self.on_click, b)

    def on_click(self, event):
        self.statictext.SetLabelText('hello world!')

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
