import tkinter as tk
import PIL
import events
import gvar as g
import mapgen as m
from math import sqrt
import threading

class make_stamp_base_thread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        m.make_new_stamp_base()


class draw_map_thread(threading.Thread):
    threadToWait = None
    def __init__(self, thread):
        threading.Thread.__init__(self)
        self.threadToWait = thread
    def run(self):
        self.threadToWait.join()
        m.draw_new_hex_map(fillhexVar.get())

class myThread (threading.Thread):
    threadsToWait = []
    func = None
    args = ()
    kwargs = {}
    def __init__(self, functorun = None, threadstowait = None, argstouse = (), kwargstouse = {}):
        if type(functorun) == type(show_new_hex):
            threading.Thread.__init__(self)
            self.func = functorun
            self.threadToWait = threadstowait
            self.args = argstouse
            self.kwargs = kwargstouse
        else:
            raise TypeError()
    def run(self):
        # threadingctr = threadingctr + 1
        for t in self.threadsToWait:
            t.join
        self.func(*self.args, **self.kwargs)


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
    g.grid_width = int(olEntry.get())

    canvas.delete("all")
    make_stamp_base_thread_inst = myThread(functorun=m.make_new_stamp_base)
    draw_map_thread_inst = myThread(functorun = m.draw_new_hex_map, threadstowait= [make_stamp_base_thread_inst,],argstouse=(fillhexVar.get(),))
    make_outline_stamp_inst = myThread(functorun = m.make_outline_stamp)
    draw_outline_thread_inst = myThread(functorun=m.draw_new_hex_grid, threadstowait= [make_outline_stamp_inst,])
    sort_thread_inst = myThread(functorun= lambda : )
    make_stamp_base_thread_inst.start()
    make_outline_stamp_inst.start()
    draw_map_thread_inst.start()
    draw_outline_thread_inst.start()
    # make_stamp = threading.Thread(group = None, target = m.make_new_stamp_base)

    # make_stamp = myThread(m.make_new_stamp_base,(),{})
    # draw_new_map = myThread(m.draw_new_hex_map,(fillhexVar.get(),),{})
    # make_stamp.start()
    # make_outline_stamp.start()
    # while(threadingctr!= 0):
        # print(threadingctr)
    # print("starting next step")
    # make_stamp.join()
    # make_outline_stamp.join()
    # m.make_new_stamp_base()
    # m.draw_new_hex_map(fillhexVar.get())
    # m.make_outline_stamp()
    # m.draw_new_hex_grid()

# new_hex_no = hide_new_hex
def debug():
    # print(g.stampbase_tc)
    canvas.delete("all")
    m.draw_new_hex_grid_bmp()
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

rowvar = tk.StringVar(value = "12")
colvar = tk.StringVar(value = "12")
pixvar = tk.StringVar(value = "48")
olvar = tk.StringVar(value="1")


rowLabel = tk.Label(newHexFrame, text = "Row")
colLabel = tk.Label(newHexFrame, text = "Column")
pixLabel = tk.Label(newHexFrame, text = "Pixel Size")
olLabel  = tk.Label(newHexFrame, text = "Outline Width")
rowEntry = tk.Spinbox(newHexFrame, exportselection = False, increment = 1, from_ = 10, textvariable = rowvar, to = 255)
colEntry = tk.Spinbox(newHexFrame, exportselection = False, increment = 1, from_ = 10, textvariable = colvar, to = 255)
pixEntry = tk.Spinbox(newHexFrame, exportselection = False, increment = 4, from_ = 8, textvariable = pixvar, to = 65536)
olEntry = tk.Spinbox(newHexFrame,exportselection = False, increment = 1, from_ = 1, to = 10, textvariable = olvar)
truecolumnVar = tk.IntVar()
truecolumnBox = tk.Checkbutton(newHexFrame, variable = truecolumnVar, text = "True Column")
# print(g.stampbase_pi_tc.keys())
valuelist = list(g.stampbase_pi_tc.keys())
valuehead = valuelist.pop()
fillhexVar = tk.StringVar(value = valuehead)
fillhexLabel = tk.Label(newHexFrame, text = "Fill Hex Type")
fillhexDD = tk.OptionMenu(newHexFrame, fillhexVar, valuehead, *valuelist)

yesButton = tk.Button(newHexFrame, text = "Confirm", command  = new_hex_yes)
noButton = tk.Button(newHexFrame, text = "Cancel", command = hide_new_hex)

rowLabel.grid(column = 1, row = 4)
colLabel.grid(column = 1, row = 5)
rowEntry.grid(column = 2, row = 4)
colEntry.grid(column = 2, row = 5)
pixLabel.grid(column = 3, row = 4)
olLabel.grid(column = 3, row = 5)
pixEntry.grid(column = 4, row = 4)
olEntry.grid(column = 4, row = 5)

truecolumnBox.grid(column = 2, row = 6)
fillhexLabel.grid(column = 3, row = 6)
fillhexDD.grid(column = 4, row = 6, sticky = tk.W)


yesButton.grid(column = 2, row  = 8)
noButton.grid(column = 4, row  = 8)