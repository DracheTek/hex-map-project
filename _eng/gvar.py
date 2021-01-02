import hexunit 
import tkinter as tk
import os
# from math import sqrt
from PIL import Image, ImageDraw, ImageTk

initflag = False

STRING = type("str")
INT = type(0)
FLOAT = type(0.0)
DOUBLE = type(0.0)
TUPLE = type((0,))
LIST = type([0,])
DICT = type({"key" :"value"})
SQRT32 = 0.86602540378443864676372317075294


truecol = True
width = 48
height = 48
height_s = lambda : int(height*SQRT32)
width_s = lambda : int(width*SQRT32)
row = 4
col = 4
alpha = 255

grid_alpha = 255
grid_width = 3

def hexpoint_tc():
    return (
    0, height_s()/2,
    width/4, 0,
    width*3/4, 0,
    width, height_s()/2,
    width*3/4, height_s(),
    width/4, height_s(),
    )

def hexpoint_tr():
    return (
    width_s()/2,0,
    width_s(), height/4,
    width_s(), height*3/4,
    width_s()/2, height,
    0,height*3/4,
    0, height/4,
    )

## hex unit base. Stores raw data and name correspondence of hex grid.

hexunitbase = {
    # "void_mark" : None,
    "water":hexunit.HexUnit("water","Water",(0,153,255)),
    "deepwater":hexunit.HexUnit("deepwater","Deep Water",(0,102,204)),
    "ocean":hexunit.HexUnit("ocean","Ocean",(0,0,255)),
    "deepocean":hexunit.HexUnit("deepocean","Deep Ocean",(0,0,102)),
    "southevergreen":hexunit.HexUnit("southevergreen","Evergreen Forest (Broad Leaf)",(0,102,0)),
    "northevergreen":hexunit.HexUnit("northevergreen","Evergreen Forest (Coniferous)",(0,51,51)),
    "mixedforest":hexunit.HexUnit("mixedforest","Mixed Forest",(0,153,0)),
    "tropicaljungle":hexunit.HexUnit("tropicaljungle","Tropical Jungle",(0,51,0)),
    "grassland":hexunit.HexUnit("grassland","Grass Land",(102,255,0)),
    "farmland":hexunit.HexUnit("farmland","Farm Land",(153,255,0)),
    "builtup":hexunit.HexUnit("builtup","Bulit Up Area",(128,128,128)),
}

## stamp base. Stores stamp (actual image) data in PIL pic form.
## tr = tc rotates 90de 
stampbase_tc = {}
stampbase_tr = {}

## thumbnail used for minimap.
## or reduce thumbnail and minimap to 4 pixels.

stampbase_tn_tc = {}
stampbase_tn_tr = {}

## stamp base in PIL PhotoImage form.

stampbase_pi_tc = {}
stampbase_pi_tr = {}

## stamp base in TK PhotoImage form. don't know if work

stampbase_tk_tc = {}
stampbase_tk_tr = {}

## grid pic in PIL and TK form

grid_pil = None
grid_tk = None
void_pil = None
void_tk = None

## icon base for future use. 
## map. correspond x-y value for table. 

mapdata = {}

def make_reg_hex_stamp(name, color):
    """
    draw regular hex stamp and nest in dictionary
    """
    colortouse = None
    if isinstance(color, hexunit.HexUnit):
        colortouse = color.color
    elif isinstance(color,tuple):
        colortouse = color
    imagebuffer = Image.new("RGBA", (width+10, height_s()+10))
    ImageDraw.Draw(imagebuffer).regular_polygon((width/2+5, height_s()/2+5, width/2),6,rotation = 0, fill = colortouse + (alpha,))
    stampbase_tc[name] = imagebuffer.copy()
    stampbase_pi_tc[name] = ImageTk.PhotoImage(stampbase_tc[name])
    # if not os.path.isdir("\\stamp"):
    #     os.makedirs("\\stamp")
    # if not os.path.isfile("\\stamp\\%s.gif"%(name,)):
    #     fd = open ("\\stamp\\%s.gif"%(name,), mode = "w")
    #     fd.close()
    # stampbase_tc[name].save("\\stamp\\%s.gif"%(name,), format = "GIF")
    # stampbase_tk_tc[name] = tk.PhotoImage("\\stamp\\%s.gif"%(name,))
    # imagebuffer = Image.new("RGBA", (width, height)
    imagebuffer = Image.new("RGBA", (height_s()+10, width+10))
    ImageDraw.Draw(imagebuffer).regular_polygon((height_s()/2+5, width/2+5, width/2),6,rotation = 90, fill = colortouse + (alpha,))
    stampbase_tr[name] = imagebuffer.copy()
    stampbase_pi_tr[name] = ImageTk.PhotoImage(stampbase_tr[name])


def make_new_stamp_base(): 
    global stampbase_tc
    global stampbase_tr
    global stampbase_pi_tc
    global stampbase_pi_tr
    """
    Turns predefined name-hexunit pair to name-stamp pair.
    """
    stampbase_tc = {}
    stampbase_tr = {}
    stampbase_pi_tc = {}
    stampbase_pi_tr = {}
    for (key, value) in hexunitbase.items():
        # draw_hex_stamp(key,value)
        make_reg_hex_stamp(key,value)

def make_outline_stamp():
    global grid_pil, grid_tk, grid_alpha, grid_width
    if truecol:
        grid_pil = Image.new("RGBA", (width+10,height_s()+10))
        pg = list(hexpoint_tc()+hexpoint_tc()[0:2:1])
        for i in range(14):
            pg[i] = pg[i] + 5
        ImageDraw.Draw(grid_pil).line(pg,fill = (0,0,0,)+(grid_alpha,), width= grid_width)
        grid_tk = ImageTk.PhotoImage(grid_pil)
    else:
        grid_pil = Image.new("RGBA", (width_s()+10,height+10))
        pg = list(hexpoint_tr()+hexpoint_tr()[0:2:1])
        for i in range (14):
            pg[i] = pg[i] + 5
        ImageDraw.Draw(grid_pil).line(pg,fill = (0,0,0,)+(grid_alpha,), width = grid_width)
        grid_tk = ImageTk.PhotoImage(grid_pil)

def make_void_stamp():
    global void_pil,void_tk
    if truecol:
        void_pil = Image.new("RGBA", (width+10, height_s()+10))
    else:
        void_pil = Image.new("RGBA", (width_s()+10, height_s+10))
    ImageDraw.Draw(void_pil).rectangle([0,0,width+10,height+10],fill =(0,0,0,0))
    void_tk = ImageTk.PhotoImage(grid_pil)
    