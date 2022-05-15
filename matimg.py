
import wx
import numpy as np
import matplotlib.pyplot as plt

class CreateImg(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
        y = np.array([1, 4, 9, 16, 7, 11, 23, 18])

        plt.scatter(x, y)
        plt.savefig('mat.png')
        # plt.show()

class LineChartExample(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(450, 600))
 
        panel = wx.Panel(self, -1)
        panel.SetBackgroundColour('RED')

        topbox = wx.BoxSizer(wx.HORIZONTAL)
        self.lbl = wx.StaticText(panel, -1, "请输入：")
        self.input = wx.TextCtrl(panel, -1)
        self.btn = wx.Button(panel, -1, "确定")
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.btn)

        # self.img = wx.Image('./1.jpeg')
        # imgbox.Add(self.img)

        topbox.Add(self.lbl)
        topbox.Add(self.input)
        topbox.Add(self.btn)
 
        hbox = wx.BoxSizer(wx.VERTICAL)
        img = CreateImg(panel)
        hbox.Add(topbox)
        hbox.Add(img, 1, wx.EXPAND | wx.ALL, 15)
        panel.SetSizer(hbox)
 
        self.Centre()
        self.Show(True)

        # plt.savefig('mat.png')
        # self.img = wx.Image('mat.png')
            
    # 定义点击事件
    def OnClick(self, event):
        inputNum = self.input.GetValue()
        print(inputNum)
 
 
app = wx.App()
LineChartExample(None, -1, 'A line chart')
app.MainLoop()