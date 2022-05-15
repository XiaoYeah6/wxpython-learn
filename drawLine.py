from distutils.filelist import translate_pattern
from tkinter.ttk import Style
import wx

class LineChart(wx.Panel): 
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.SetBackgroundColour('WHITE')
 
        self.Bind(wx.EVT_PAINT, self.OnPaint)
 
    def OnPaint(self, event):
        dc = wx.PaintDC(self)
        dc.SetDeviceOrigin(40, 240)
        dc.SetAxisOrientation(True, True)
        dc.SetPen(wx.Pen('BLACK'))
        # self.DrawAxis(dc)
        self.DrawShip(dc)

    # 绘制坐标轴
    # def DrawAxis(self, dc):
    #     dc.SetPen(wx.Pen('#0AB1FF'))
    #     font = dc.GetFont()
    #     font.SetPointSize(8)
    #     dc.SetFont(font)
    #     dc.DrawLine(-10, 0, 300, 0)
    #     dc.DrawLine(0, -200, 0, 200)

    #     # 绘制纵坐标间隔
    #     for i in range(-200, 201, 10):
    #         dc.DrawText(str(i), -30, i+5)
    #         dc.DrawLine(2, i, -3, i)
 
    #     for i in range(10, 300, 10):
    #         dc.DrawLine(i, 2, i, -3)
 
    def DrawShip(self, dc):
        dc.SetPen(wx.Pen('#BLACK'))
        font = dc.GetFont()
        font.SetPointSize(8)
        dc.SetFont(font)
        # 船体
        dc.DrawLine(100, 20, 100, -20)
        dc.DrawLine(100, 20, 200, 20)
        dc.DrawLine(100, -20, 200, -20)
        dc.DrawLine(200, 20, 250, 0)
        dc.DrawLine(200, -20, 250, 0)

        dc.SetPen(wx.Pen('gray', width=1))
        # 船尾部
        dc.DrawLine(100, 20, 0, 60)
        dc.DrawLine(100, -20, 0, -60)
        
        # 船侧部
        dc.DrawLine(200, 20, 180, 60)
        dc.DrawLine(180, 60, 0, 110)
        dc.DrawLine(200, -20, 180, -60)
        dc.DrawLine(180, -60, 0, -110)

        # 
        dc.DrawLine(160, 20, 120, 100)
        dc.DrawLine(120, 20, 60, 140)
        dc.DrawLine(160, -20, 120, -100)
        dc.DrawLine(120, -20, 60, -140)

        # 
        dc.DrawLine(70, 32, 70, -32)
        dc.DrawLine(40, 44, 40, -44)
        dc.DrawLine(10, 56, 10, -56)
        dc.DrawLine(99, 20, 99, -20)

        dc.SetBrush(wx.Brush('red'))
        dc.FloodFill(15, 0, 'gray', style=wx.FLOOD_BORDER)

        dc.SetBrush(wx.Brush('yellow'))
        dc.FloodFill(45, 0, 'gray', style=wx.FLOOD_BORDER)

        dc.SetBrush(wx.Brush('green'))
        dc.FloodFill(75, 0, 'gray', style=wx.FLOOD_BORDER)
 
class LineChartExample(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(450, 600))
 
        self.panel = wx.Panel(self, -1)
        self.panel.SetBackgroundColour('WHITE')

        topbox = wx.BoxSizer(wx.HORIZONTAL)
        self.lbl = wx.StaticText(self.panel, -1, "请输入Fn: ")
        self.input = wx.TextCtrl(self.panel, -1)
        self.btn = wx.Button(self.panel, -1, "确定")
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.btn)

        topbox.Add(self.lbl)
        topbox.Add(self.input)
        topbox.Add(self.btn)
 
        self.hbox = wx.BoxSizer(wx.VERTICAL)
        linechart = LineChart(self.panel)
        self.hbox.Add(topbox)
        self.hbox.Add(linechart, 1, wx.EXPAND | wx.ALL, 15)
        self.panel.SetSizer(self.hbox)
 
        self.Centre()
        self.Show(True)
    # 定义点击事件
    def OnClick(self, event):
        inputNum = self.input.GetValue()
        print(inputNum)
    #     linechart = LineChart(self.panel)
    #     self.hbox.Add(linechart, 1, wx.EXPAND | wx.ALL, 15)
    #     self.panel.SetSizer(self.hbox)
    #     self.panel.Update()
 
 
app = wx.App()
LineChartExample(None, -1, 'Program')
app.MainLoop()
