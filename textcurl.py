from multiprocessing import parent_process
from turtle import title
import wx

data = ((10, 9), (20, 22), (30, 21), (40, 30), (50, 41),
(60, 53), (70, 45), (80, 20), (90, 19), (100, 22),
(110, 42), (120, 62), (130, 43), (140, 71), (150, 89),
(160, 65), (170, 126), (180, 187), (190, 128), (200, 125),
(210, 150), (220, 129), (230, 133), (240, 134), (250, 165),
(260, 132), (270, 130), (280, 159), (290, 163), (300, 94))
 
years = ('2003', '2004', '2005')

class Chart(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.SetBackgroundColour('BLACK')

        # self.Bind(wx.EVT_PAINT, self.OnPaint)

        def OnPaint(self, event):
            dc = wx.PaintDC(self)
            dc.SetPen(wx.Pen('#d4d4d4'))
 
            dc.SetBrush(wx.Brush('#c56c00'))
            dc.DrawRectangle(10, 15, 90, 60)



class myFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="123", size=(450, 400))

        # 创建面板
        panel = wx.Panel(self, -1)
        toppanel = wx.Panel(self, -1)
        bottompanel = wx.Panel(self,-1)
        self.SetBackgroundColour('WHITE')

        # 创建sizer
        mainbox = wx.BoxSizer(wx.VERTICAL)
        tbox = wx.BoxSizer(wx.HORIZONTAL)
        bbox = wx.BoxSizer()

        chart = Chart(bottompanel)
        bbox.Add(chart, wx.EXPAND)

        # 创建组件
        lbl = wx.StaticText(toppanel, -1, "请输入：")
        self.num = wx.TextCtrl(toppanel, -1, "", size=(-1, 25))
        self.serachBtn = wx.Button(toppanel, -1, "确定")
        # self.Bind(wx.EVT_BUTTON, self.OnClick, self.serachBtn)

        mainsizer = wx.BoxSizer(wx.HORIZONTAL)

        mainsizer.Add(lbl)
        mainsizer.Add(self.num, wx.EXPAND)
        mainsizer.Add(self.serachBtn)

        tbox.Add(mainsizer, wx.EXPAND)

        mainbox.Add(tbox, wx.EXPAND)
        # mainbox.Add(bbox, wx.EXPAND)

        panel.SetSizer(tbox)


if __name__ == '__main__':
    app = wx.App()
    frame = myFrame()
    frame.Show()
    app.MainLoop()