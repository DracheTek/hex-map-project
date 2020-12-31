import tkinter as tk
import PIL
import events
import gvar as g
import mapgen as m

def show_new_hex():
    newHexFrame.deiconify()

def hide_new_hex():
    newHexFrame.withdraw()

def new_hex_yes():
    """

    绘制新图的流程：
    读对话框所有内容
    按照对话框所给的大小重绘所有印章
    擦除画布
    按照对话框所给行列重绘地图
    按照对话框所给行列重绘地图网格
    """
    g.width = int(pixEntry.get())
    g.height = int(pixEntry.get())
    g.row = int(rowEntry.get())
    g.col = int(colEntry.get())
    g.truecol = bool(truecolumnVar.get())
    # print(g.width)
    # print(g.height)
    # print(g.row)
    # print(g.col)
    # print(g.truecol)
    m.make_new_stamp_base()
    m.draw_new_hex_map(fillhexVar.get())
    pass

# new_hex_no = hide_new_hex
def debug():
    print(g.stampbase_tc)
    pass

#### Definition for top level windows



top = tk.Tk()
top.title("Canvas Test")
top.geometry("1366x768")

top.bind("<Configure>", events.onResizingMain)

m.make_new_stamp_base()

toolbar = tk.Canvas(top)
toolbar.grid(sticky = tk.W)

canvas = tk.Canvas(top, width = 1300, height = 700)
canvas.grid()

filebutton = tk.Menubutton(toolbar, text = "File")
filebutton.grid(sticky = tk.W)

filemenu = tk.Menu(filebutton, tearoff= 0)
filebutton.menu = filemenu
filebutton['menu'] = filemenu
filemenu.add_command(label = "NEW",command = show_new_hex)

debugbutton = tk.Button(top, text = "Debug", command = debug)
debugbutton.grid()

#### definition for new map dialog box

newHexFrame = tk.Toplevel(menu = 0)
newHexFrame.withdraw()
newHexFrame.geometry("500x300")
newHexFrame.protocol("WM_DELETE_WINDOW", hide_new_hex)
newHexFrame.resizable(False,False)

rowLabel = tk.Label(newHexFrame, text = "Row")
colLabel = tk.Label(newHexFrame, text = "Column")
pixLabel = tk.Label(newHexFrame, text = "Pixel Size")
rowEntry = tk.Spinbox(newHexFrame, exportselection = False, increment = 1, from_ = 2, to = 255)
colEntry = tk.Spinbox(newHexFrame, exportselection = False, increment = 1, from_ = 2, to = 255)
pixEntry = tk.Spinbox(newHexFrame, exportselection = False, increment = 4, from_ = 12, to = 65532)
truecolumnVar = tk.IntVar()
truecolumnBox = tk.Checkbutton(newHexFrame, variable = truecolumnVar, text = "True Column")
fillhexVar = tk.StringVar()
# print(g.stampbase_pi_tc.keys())
valuelist = list(g.stampbase_pi_tc.keys())
valuehead = valuelist.pop()
fillhexLabel = tk.Label(newHexFrame, text = "Fill Hex Type")
fillhexDD = tk.OptionMenu(newHexFrame, fillhexVar, valuehead, *valuelist)
fillhexVar.set(valuehead)

yesButton = tk.Button(newHexFrame, text = "Confirm", command  = new_hex_yes)
noButton = tk.Button(newHexFrame, text = "Cancel", command = hide_new_hex)

rowLabel.grid(column = 1, row = 4)
colLabel.grid(column = 1, row = 5)
rowEntry.grid(column = 2, row = 4)
colEntry.grid(column = 2, row = 5)
pixLabel.grid(column = 3, row = 4)
pixEntry.grid(column = 4, row = 4)

truecolumnBox.grid(column = 2, row = 6)
fillhexLabel.grid(column = 3, row = 6)
fillhexDD.grid(column = 4, row = 6, sticky = tk.W)


yesButton.grid(column = 2, row  = 8)
noButton.grid(column = 4, row  = 8)