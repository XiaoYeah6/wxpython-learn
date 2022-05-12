import numpy
import wx
import wx.lib.plot as wxPyPlot #导入绘图模块,并命名为wxPyPlot
  
#---------------------------------------------------------------------------
# 需要把数据封装进入MyDataObject中
def MyDataObject():
 # 50 个点的sin函数,用蓝色圆点表示
 data1 = 2.*numpy.pi*numpy.arange(100)/100.
 data1.shape = (50, 2)
 data1[:,1] = numpy.sin(data1[:,0])
 markers = wxPyPlot.PolyMarker(data1, legend='Green Markers', colour='blue', marker='circle',size=1)
  
 # 50个点的cos函数,用红色表示
 data2 = 2.*numpy.pi*numpy.arange(100)/100.
 data2.shape = (50,2)
 data2[:,1] = numpy.cos(data2[:,0])
 lines = wxPyPlot.PolySpline(data2, legend= 'Red Line', colour='red')
  
 GraphTitle="Plot Data(Sin and Cos)"
  
  
 return wxPyPlot.PlotGraphics([markers, lines],GraphTitle, "X Axis", "Y Axis")
#-----------------------------------------------------------------------------
class TestFrame1(wx.Frame):
 def __init__(self, parent=None, id=wx.ID_ANY, title="Using wxPyPlot"):
  wx.Frame.__init__(self, parent, id, title,size=(600, 400))
   
  # 创建菜单栏
  self.mainmenu = wx.MenuBar()
  
  menu = wx.Menu()
  menu.Append(100, 'Draw1', 'Draw plots1')
  self.Bind(wx.EVT_MENU,self.OnPlotDraw1, id=100)
  
  self.mainmenu.Append(menu, '&Plot')
  
  self.SetMenuBar(self.mainmenu)
  
  # 创建状态栏,显示信息
  self.CreateStatusBar(2)
   
  self.pc = wxPyPlot.PlotCanvas(self) #此处导入绘图面板
  
 def OnPlotDraw1(self, event): #绘图函数
  self.pc.Draw(MyDataObject())
  
  
###########################################################################
## 测试wxPyPlot的代码
###########################################################################
if __name__=='__main__':
  app = wx.App()
  tf=TestFrame1(None)
  tf.Show()
  app.MainLoop()