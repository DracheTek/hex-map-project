import tkinter as tk
import tkinter.filedialog as tkfd
import mapgen as m
import frame as f
import mythread as t
import gvar as g

readdatatype = "none"

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

    f.canvas.delete("all")
    make_stamp_base_thread_inst = t.myThread("make stamp", functorun=g.make_new_stamp_base)
    draw_map_thread_inst = t.myThread("draw map", functorun = m.draw_new_hex_map, threadstowait= [make_stamp_base_thread_inst,],argstouse=(valuelist[fillhexVar.get()],))
    make_outline_stamp_inst = t.myThread("make outline stamp", functorun = g.make_outline_stamp)
    draw_outline_thread_inst = t.myThread("draw outline",functorun=m.draw_new_hex_grid, threadstowait= [make_outline_stamp_inst])
    sort_thread_inst = t.myThread("sort layer", functorun= f.sort_layer, threadstowait= [draw_map_thread_inst, draw_outline_thread_inst,])
    make_stamp_base_thread_inst.start()
    make_outline_stamp_inst.start()
    draw_map_thread_inst.start()
    draw_outline_thread_inst.start()

    # g.make_new_stamp_base()
    # m.draw_new_hex_map(fillhexVar.get(),canvas)

    # g.make_outline_stamp()
    # m.draw_new_hex_grid()
    sort_thread_inst.start()
    filemenu.entryconfig(1,state = tk.NORMAL)
    sr = (0,0,g.width_s()*g.col,g.height*g.row*3/4+g.height/4) if not g.truecol else (0,0,g.width*(g.col/3*4+1/4),g.height_s()*g.row)
    f.canvas.config(scrollregion = sr)
    newHexFrame.withdraw()
    # new_hex_th_inst = t.myThread("Make new inst", new_hex_yes_th)
    # new_hex_th_inst.start()

def import_data():
    importfile = tkfd.askopenfile(mode = "r", defaultextension = ".txt", filetypes = [("TXT file", "*.txt")])
    if (importfile != None):
        filestring = importfile.read()
    pass

def export_map():
    exportFile = None
    # print(len(g.mapdata))
    if (len(g.mapdata) != 0):
        exportFile = tkfd.asksaveasfile(mode = "w",defaultextension = ".txt", filetypes = [("TXT file","*.txt"),])
        # exportFile.isopen
        if (exportFile != None):
            exportFile.write("hexunitdef\n")
            for p in g.hexunitbase.items():
                name = p[0]
                displayname = p[1].displayname
                color = p[1].color
                exportFile.write(name+","+str(color[0])+","+str(color[1])+","+str(color[2])+"\n")
            exportFile.write("coorddef\n")
            for p in g.mapdata.items():
                x= p[0][0]
                y= p[0][1]
                name = p[1]
                exportFile.write(str(x)+","+str(y)+","+name+"\n")
            exportFile.close()
    # print(exportPath)
    pass


filebutton = tk.Menubutton(f.toolbar, text = "File")
other1button = tk.Menubutton(f.toolbar, text = "Other1")
other2button = tk.Menubutton(f.toolbar, text = "Other2")
filebutton.grid(column = 0, row = 0)
other1button.grid(column = 1, row = 0)
other2button.grid(column = 2, row = 0)

filemenu = tk.Menu(filebutton, tearoff= 0)
filebutton.menu = filemenu
filebutton['menu'] = filemenu
filemenu.add_command(label = "NEW",command = show_new_hex)
filemenu.add_command(label = "EXPORT", command = export_map, state = tk.DISABLED)

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
valuelist = {} # key:name value:displayname
for v in g.hexunitbase.values():
    valuelist[v.displayname] = v.name
# valuehead = valuelist.popitem()
fillhexVar = tk.StringVar(value = list(valuelist.keys())[0])
fillhexLabel = tk.Label(newHexFrame, text = "Fill Hex Type")
fillhexDD = tk.OptionMenu(newHexFrame, fillhexVar, list(valuelist.keys())[0], *tuple(valuelist.keys())[1:-1:1])

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




