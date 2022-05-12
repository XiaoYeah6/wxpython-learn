
import numpy
from numpy import size
import wx
import wx.lib.plot as wxPyPlot #导入绘图模块,并命名为wxPyPlot

def MyDataObject():
 # 50个点的cos函数,用红色表示
    data2 = 2.*numpy.pi*numpy.arange(100)/100.
    data2.shape = (50,2)
    data2[:,1] = numpy.cos(data2[:,0])
    lines = wxPyPlot.PolySpline(data2, legend= 'Red Line', colour='red')
    GraphTitle="Plot Data(Sin and Cos)"
    return wxPyPlot.PlotGraphics(lines,GraphTitle, "X Axis", "Y Axis")

class myFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="Program", size=(500, 600), pos=(200, 200))
        panel = wx.Panel(self)

        # 创建组件
        lbl = wx.StaticText(panel, -1, "请输入：")
        self.num = wx.TextCtrl(panel, -1, "", size=(-1, 25))
        self.serachBtn = wx.Button(panel, -1, "确定")
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.serachBtn)

        self.inputNum = wx.StaticText(panel, -1, "")
        
        # 主要布局
        mainsizer = wx.BoxSizer(wx.VERTICAL)
        topsizer = wx.BoxSizer(wx.HORIZONTAL)
        lblsizer = wx.BoxSizer(wx.VERTICAL)
        inputsizer = wx.BoxSizer(wx.VERTICAL)
        btnsizer = wx.BoxSizer(wx.VERTICAL)
        imgsizer = wx.BoxSizer()
        mainsizer.Add(topsizer, 1, wx.EXPAND)
        mainsizer.Add(imgsizer, 5, wx.EXPAND)

        # 顶部布局
        lblsizer.Add(lbl, wx.ALIGN_RIGHT)
        inputsizer.Add(self.num)
        btnsizer.Add(self.serachBtn)

        topsizer.Add(lblsizer)
        topsizer.Add(inputsizer, wx.EXPAND)
        topsizer.Add(btnsizer)

        # 图片部分布局
        self.CreateStatusBar(2)
        # self.pc = wxPyPlot.PlotCanvas(self) #此处导入绘图面板

        panel.SetSizer(mainsizer)

    def OnPlotDraw1(self, event): #绘图函数
        self.pc.Draw(MyDataObject())

    # 定义点击事件，获取输入的数字
    def OnClick(self, event):
        input = self.num.GetValue()
        print(input)
        self.inputNum.SetLabelText(input)

if __name__ == '__main__':
    app = wx.App()
    frame = myFrame()
    frame.Show()
    app.MainLoop()
