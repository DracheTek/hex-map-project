from PIL import Image, ImageDraw, ImageTk
import tkinter as tk
import gvar as g
import frame as f
import hexunit as h
import mythread as t
from math import sqrt,floor,ceil

def import_stamp_base(filename, wipe = True):
    """
    Read file name or file object and update stamp base. if Wipe is true, make new stamp base. 
    """
    pass

def draw_new_map_data(name):
    """
    draw new map data(coordinate/color correspondance)
    """
    g.mapdata = {}
    for c in range (g.col):
        # mapcol = {}
        for r in range(g.row):
            g.mapdata[(c,r)] = name
        # g.mapdata.append(mapcol)

def draw_new_map_th(data):
    for d in data:
        # print(d)
        name = d[1]
        x = d[0][0]
        y = d[0][1]
        if g.truecol:
            stamp = g.stampbase_pi_tc[name]
            xpos = int(g.width*(x+1)*3/4)
            ypos = int(g.height_s()*(y+1+(x%2)/2))
        else:
            stamp = g.stampbase_pi_tr[name]
            xpos = int(g.width_s()*(x+1+(y%2)/2))
            ypos = int(g.height*(y+1)*3/4)
        f.canvas.create_image((xpos,ypos), image = stamp, anchor = tk.NW, tags = ("terrain", "x"+str(x),"y"+str(y),))
        f.canvas.create_polygon(xpos,ypos)

def draw_new_map():
    """
    draw map according to map data
    """
    threadlist = []
    datalistlist = []
    mapdatacopy = list(g.mapdata.items())
    for r in range(g.row):
        datalistlist.append([])
        for c in range(g.col):
            datalistlist[r].append(mapdatacopy.pop())
    for p in datalistlist:
        threadlist.append(t.myThread("draw map row",draw_new_map_th,[],(p,),{}))
        threadlist[-1].start()
        # x = p[0][0]
        # y = p[0][1]
        # name = p[1]
        # if g.truecol:
        #     stamp = g.stampbase_pi_tc[p[1]]
        #     xpos = int(g.width*(p[0][0]+1)*3/4)
        #     ypos = int(g.height_s()*(p[0][1]+1+(p[0][0]%2)/2))
        # else:
        #     stamp = g.stampbase_pi_tr[p[1]]
        #     xpos = int(g.width_s()*(p[0][0]+1+(p[0][1]%2)/2))
        #     ypos = int(g.height*(p[0][1]+1)*3/4)
        # f.canvas.create_image((xpos,ypos), image = stamp, anchor = tk.NW, tags = ("terrain", "x"+str(x),"y"+str(y),))

def draw_new_hex_map(name):
    """
    fill a new map with given width and height.
    """
    draw_new_map_data(name)
    draw_new_map()
    # if g.truecol:
    #     stamp = g.stampbase_pi_tc[name]
    #     for c in range(g.col):
    #         for r in range (g.row):
    #             f.canvas.create_image(int(g.width*(c+1)*3/4), int(g.height_s()*(r+1+(c%2)/2)), image = stamp, anchor = tk.NW,tags = ("terrain",))
    # else:
    #     stamp = g.stampbase_pi_tr[name]
    #     for r in range(g.row):
    #         for c in range (g.col):
    #             f.canvas.create_image(int(g.height_s()*(c+1+(r%2)/2)), int(g.width*(r+1)*3/4), image = stamp, anchor = tk.NW,tags = ("terrain",))

def draw_new_hex_grid():
    """
    draw a new map grid with given width and height.
    """
    # while (g.grid_tk == None):
    #     continue
    if g.truecol:
        for c in range (g.col):
            for r in range (g.row):
                f.canvas.create_image(int(g.width*(c+1)*3/4), int(g.height_s()*(r+1+(c%2)/2)), image = g.grid_tk, anchor = tk.NW, tags = ("outline",))
    else:
        for r in range (g.row):
            for c in range (g.col):
                f.canvas.create_image(int(g.width_s()*(c+1+(r%2)/2)), int(g.height*(r+1)*3/4), image = g.grid_tk, anchor = tk.NW, tags = ("outline",))
