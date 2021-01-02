import tkinter as tk
import PIL
import frame
import gvar as g

def onResizingMain(event):
    if not g.initflag :
        g.initflag = True
        print("Initialized")
    w = frame.top.winfo_width()
    h = frame.top.winfo_height()
    frame.canvas.config(width = w-100, height= h-100)
    frame.x = frame.canvas.winfo_width()
    frame.y = frame.canvas.winfo_height()
    # print("Resizing Main Window")