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
        dc.SetPen(wx.Pen('WHITE'))
 
 
class LineChartExample(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(450, 400))
 
        panel = wx.Panel(self, -1)
        panel.SetBackgroundColour('RED')

        topbox = wx.BoxSizer(wx.HORIZONTAL)
        self.lbl = wx.StaticText(panel, -1, "请输入：")
        self.input = wx.TextCtrl(panel, -1)
        self.btn = wx.Button(panel, -1, "确定")
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.btn)

        topbox.Add(self.lbl)
        topbox.Add(self.input)
        topbox.Add(self.btn)
 
        hbox = wx.BoxSizer(wx.VERTICAL)
        linechart = LineChart(panel)
        hbox.Add(topbox)
        hbox.Add(linechart, 1, wx.EXPAND | wx.ALL, 15)
        panel.SetSizer(hbox)
 
        self.Centre()
        self.Show(True)
    # 定义点击事件
    def OnClick(self, event):
        inputNum = self.input.GetValue()
        print(inputNum)
 
 
app = wx.App()
LineChartExample(None, -1, 'A line chart')
app.MainLoop()