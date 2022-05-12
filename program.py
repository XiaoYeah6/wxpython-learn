
from numpy import size
import wx

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
        img = wx.Image("1.jpeg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        show3 = wx.StaticBitmap(self, -1, img, pos=(0,100), size=(500, 500))
        imgsizer.Add(show3, 0)


        panel.SetSizer(mainsizer)


    # 定义点击事件，获取输入的数字
    def OnClick(self, event):
        input = self.num.GetValue()
        print(input)
        self.inputNum.SetLabelText(input)


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
