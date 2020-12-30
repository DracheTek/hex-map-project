import tkinter as tk
import PIL
import events

top = tk.Tk()
top.title("Canvas Test")
top.geometry("1366x768")

top.bind("<Configure>", events.onResizingMain)

toolbar = tk.Canvas(top)
toolbar.grid(sticky = tk.W)

filebutton = tk.Menubutton(toolbar, text = "File")
filebutton.grid(sticky = tk.W)

filemenu = tk.Menu(filebutton, tearoff= 0)
filebutton.menu = filemenu
filebutton['menu'] = filemenu
filemenu.add_command(label = "NEW")

newHexFrame = tk.Toplevel()
newHexFrame.geometry("600x400")

# rowLabel = tk.Label(newHexFrame)
# colLabel = tk.Label(newHexFrame, text = "Column")
# pixLabel = tk.Label(newHexFrame, text = "Pixel Size")
rowEntry = tk.Entry(newHexFrame, exportselection = False)
colEntry = tk.Entry(newHexFrame, exportselection = False)
pixEntry = tk.Entry(newHexFrame, exportselection = False)
truecolumnBox = tk.Checkbutton(newHexFrame)

yesButton = tk.Button()
noButton = tk.Button()

