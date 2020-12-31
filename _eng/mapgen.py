from PIL import Image, ImageDraw, ImageTk
import tkinter as tk
import gvar as g
import frame as f
import hexunit as h

def draw_hex_stamp(name, color):
    """
    draw a hex stamp and nest it in dictionary.
    """
    # if g.truecol:
    colortouse = None
    # if isinstance(name, str):
        # raise TypeError("Name must be a string")
    if isinstance(color, h.HexUnit):
        colortouse = color.color
    elif isinstance(color, tuple):
        colortouse = color
    imagebuffer = Image.new("RGBA", (g.width, g.height))
    ImageDraw.Draw(imagebuffer).polygon(g.hexpoint_tc(),fill = colortouse + (g.alpha,))
    g.stampbase_tc[name] = imagebuffer.copy()
    g.stampbase_pi_tc[name] = ImageTk.PhotoImage(g.stampbase_tc[name])
    imagebuffer = Image.new("RGBA", (g.width, g.height))
    ImageDraw.Draw(imagebuffer).polygon(g.hexpoint_tr(),fill = colortouse + (g.alpha,))
    g.stampbase_tr[name] = imagebuffer.copy()
    g.stampbase_pi_tr[name] = ImageTk.PhotoImage(g.stampbase_tr[name])

    # else:

def make_new_stamp_base(): 
    """
    Turns predefined name-hexunit pair to name-stamp pair.
    """
    g.stampbase_tc = {}
    g.stampbase_tr = {}
    g.stampbase_pi_tc = {}
    g.stampbase_pi_tr = {}
    for (key, value) in g.hexunitbase.items():
        draw_hex_stamp(key,value)

def import_stamp_base(filename, wipe = True):
    """
    Read file name or file object and update stamp base. if Wipe is true, make new stamp base. 
    """
    pass

def draw_new_hex_map(name):
    """
    fill a new map with given width and height.
    """
    # pass
    # return
    f.canvas.delete("all")
    stamp = g.stampbase_pi_tc[name]
    for r in range(g.row):
        for c in range (g.col):
            f.canvas.create_image(g.width*(r+1)*3/4, g.height*(c+1+(r%2)/2), image = stamp, anchor = tk.NW)