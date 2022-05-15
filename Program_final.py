from distutils.filelist import translate_pattern
from tkinter.ttk import Style
from numpy import size
import wx, time

class CreateImg(wx.Panel): 
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        
 

class Frame(wx.Frame):
    def __init__(self,parent = None,id = -1,title ='系统管理界面'):
        wx.Frame.__init__(self,parent,id,title,size=(400, 450))
        self.panel_white = None
        self.panel_image = None
        self.setupStatusBar()
        self.InitBottom()
        self.InitTop()

    #初始化状态栏
    def setupStatusBar(self):
        # 状态栏
        sb = self.CreateStatusBar(2)  # 2代表将状态栏分为两个
        self.SetStatusWidths([-1, -2])  # 比例为1：2
        self.SetStatusText("Ready", 0)  # 0代表第一个栏，Ready为内容
        # timmer
        self.timer = wx.PyTimer(self.Notify)
        self.timer.Start(1000, wx.TIMER_CONTINUOUS)
        self.Notify()

    # 实时显示时间
    def Notify(self):
        t = time.localtime(time.time())
        st = time.strftime('%Y-%m-%d %H:%M:%S', t)
        self.SetStatusText(st, 1)  # 这里的1代表将时间放入状态栏的第二部分上
 
    def InitTop(self):
        self.panel_top = wx.Panel(self, pos=(0, 0), size=(400, 50))
        self.panel_top.SetBackgroundColour('WHITE')

        self.lbl = wx.StaticText(self.panel_top, -1, "请输入Fn: ", pos=(30, 15), size=(60, 30))
        self.input = wx.TextCtrl(self.panel_top, -1, pos=(100, 10), size=(150, 30))
        self.btn = wx.Button(self.panel_top, -1, "确定", pos=(260, 10), size=(50, 30))
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.btn)

    def InitBottom(self):
        self.panel_white = wx.Panel(self, pos=(0, 50), size=(400, 400))
        # self.panel_white.SetBackgroundColour('RED')


    # 定义点击事件
    def OnClick(self, event):
        inputNum = self.input.GetValue()
        print(inputNum)
        if inputNum == '':
            if self.panel_image:
                self.panel_image.Destroy()
                self.InitBottom()
            print('请输入Fn')
        if inputNum != '':
            if self.panel_white:
                self.panel_white.Destroy()
            self.panel_image = wx.Panel(self, pos=(0, 50), size=(400, 350))
            self.panel_image.Bind(wx.EVT_PAINT, self.OnPaint)
 
    def OnPaint(self, event):
        dc = wx.PaintDC(self.panel_image)
        dc.SetDeviceOrigin(40, 160)
        dc.SetAxisOrientation(True, True)
        dc.SetPen(wx.Pen('BLACK'))
        self.DrawShip(dc)
 
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






            # imagebox = wx.BoxSizer(wx.VERTICAL)
            # image = CreateImg(self.panel_image, 1, wx.EXPAND | wx.ALL)
            # imagebox.Add(image)
            # self.panel_image.SetSizer(imagebox)
            # self.Centre()
            # self.Show(True)


class App(wx.App): #5 wx.App子类
    def __init__(self):
    #如果要重写__init__,必须调用wx.App的__init__,否则OnInit方法不会被调用
        wx.App.__init__(self)
    def OnInit(self):
        self.frame=Frame()
        self.frame.Show()

        return True

if __name__=="__main__":
    app = App()
    app.MainLoop()
