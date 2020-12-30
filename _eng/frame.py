import tkinter as tk
import PIL
import events
import gvar

def show_new_hex():
    newHexFrame.deiconify()

def hide_new_hex():
    newHexFrame.withdraw()

top = tk.Tk()
top.title("Canvas Test")
top.geometry("1366x768")

top.bind("<Configure>", events.onResizingMain)

toolbar = tk.Canvas(top)
toolbar.grid(sticky = tk.W)

canvas = tk.Canvas(top, width = 1300, height = 700)

filebutton = tk.Menubutton(toolbar, text = "File")
filebutton.grid(sticky = tk.W)

filemenu = tk.Menu(filebutton, tearoff= 0)
filebutton.menu = filemenu
filebutton['menu'] = filemenu
filemenu.add_command(label = "NEW",command = show_new_hex)

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
truecolumnBox = tk.Checkbutton(newHexFrame)

yesButton = tk.Button(newHexFrame, text = "Confirm")
noButton = tk.Button(newHexFrame, text = "Cancel", command = hide_new_hex)

rowLabel.grid(column = 1, row = 4)
colLabel.grid(column = 1, row = 5)
rowEntry.grid(column = 2, row = 4)
colEntry.grid(column = 2, row = 5)
pixLabel.grid(column = 3, row = 4)
pixEntry.grid(column = 4, row = 4)
yesButton.grid(column = 2, row  = 8)
noButton.grid(column = 4, row  = 8)