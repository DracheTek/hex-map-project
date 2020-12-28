import turtle
from tkinter import *
from PIL import ImageTk, Image

top = Tk() #主窗口。
top.title("Hex Grid Maker") #窗口的标题
top.geometry("1600x900") #窗口的几何构型，格式是宽乘（小写x）高


## 菜单包含两类：菜单按钮（Menubutton()）和下拉/弹出菜单(Menu())

filebutton = Menubutton(top, text = "File")
filebutton.grid() #让控件显示在屏幕上。
filemenu = Menu(filebutton ,tearoff = 0)
filebutton.menu = filemenu
filebutton['menu'] = filemenu

""" 下拉菜单包括五种可选内容：
Cascade: 折叠菜单。点击显示另一组菜单
command: 指令。执行一个指令。
checkbutton: 复选按钮
radiobutton: 单选按钮
separator: 分割线
 """
filemenu.add_command(label = "New ...")
filemenu.add_command(label = "Load ...")
filemenu.add_command(label = "Save ...")
filemenu.add_command(label = "Import ...")
filemenu.add_command(label = "Export ...")

mainmenu = Menu()


top.mainloop()
