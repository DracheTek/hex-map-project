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
    frame.canvas.config(width = w, height= h)
    print("Resizing Main Window")