
import numpy
from numpy import size
import wx
import wx.lib.plot as wxPyPlot #导入绘图模块,并命名为wxPyPlot

def MyDataObject():
    data2 = 2.*numpy.pi*numpy.arange(100)/100.
    data2.shape = (50,2)
    data2[:,1] = numpy.cos(data2[:,0])
    lines = wxPyPlot.PolySpline(data2, legend= 'Red Line', colour='red')
    GraphTitle="Plot Data(Sin and Cos)"
    return wxPyPlot.PlotGraphics(lines,GraphTitle, "X Axis", "Y Axis")

class ImgWindow(wx.Window):
    def __init__(self, parent, ID):
        super().__init__()
        self.SetBackgroundColour("White")
        self.pos = (0, 0)
        

class myFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="Program", size=(500, 600), pos=(200, 200))
        self.imgWindow = ImgWindow(self, -1)
        toppanel = wx.Panel(self)

        # 创建组件
        self.lbl = wx.StaticText(toppanel, -1, "请输入：")
        self.num = wx.TextCtrl(toppanel, -1, "")
        self.searchBtn = wx.Button(toppanel, -1, "确定")
        # self.Bind(wx.EVT_BUTTON, self.OnClick, self.searchBtn)


        # 主要布局
        mainsizer = wx.BoxSizer(wx.VERTICAL)
        topsizer = wx.BoxSizer(wx.HORIZONTAL)
        # lblsizer = wx.BoxSizer(wx.VERTICAL)
        # inputsizer = wx.BoxSizer(wx.VERTICAL)
        # btnsizer = wx.BoxSizer(wx.VERTICAL)

        # 顶部布局
        # lblsizer.Add(self.lbl, wx.EXPAND)
        # inputsizer.Add(self.num, wx.EXPAND)
        # btnsizer.Add(self.searchBtn, wx.EXPAND)

        mainsizer.Add(topsizer, wx.EXPAND)
        topsizer.Add(self.lbl)
        topsizer.Add(self.num)
        topsizer.Add(self.searchBtn)

        toppanel.SetSizer(mainsizer)

        box = wx.BoxSizer(wx.VERTICAL)
        box.Add(toppanel, 1, wx.EXPAND)
        box.Add(self.imgWindow, 3, wx.EXPAND)

        self.SetSizer(box)

if __name__ == '__main__':
    app = wx.App()
    frame = myFrame()
    frame.Show()
    app.MainLoop()
