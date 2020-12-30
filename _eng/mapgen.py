from PIL import Image, ImageDraw, ImageTk
import tkinter as tk
import gvar

def draw_hex_stamps(name, color):
    # if gvar.truecol:
    if type(name) is not "string":
        raise TypeError("Name must be a string")
    imagebuffer = Image.new("RGBA", (gvar.width, gvar.height))
    ImageDraw.Draw(imagebuffer).polygon(gvar.hexpoint_tc,fill = color + (gvar.alpha))
    gvar.stampbase_tc[name] = Image.copy()
    # else:
