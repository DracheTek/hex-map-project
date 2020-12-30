import tkinter as tk
import PIL
import frame

def onResizingMain(event):
    w = top.winfo_width()
    h = top.winfo_height()
    canvas.config(width = w, height= h)
    print("Resizing Main Window")