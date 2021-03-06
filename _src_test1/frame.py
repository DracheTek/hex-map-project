import tkinter as tk
import tkinter.filedialog as tkfd
import PIL
# import events
# import gvar as g
# import mapgen as m
import mythread as t
import time

"""Bind to this widget at event SEQUENCE a call to function FUNC.

SEQUENCE is a string of concatenated event
patterns. An event pattern is of the form
<MODIFIER-MODIFIER-TYPE-DETAIL> where MODIFIER is one
of 
Control, 
Mod2, 
M2, 
Shift, 
Mod3, 
M3, 
Lock, 
Mod4, 
M4,
Button1, 
B1, 
Mod5, 
M5 
Button2, 
B2, 
Meta, 
M, 
Button3,
B3, 
Alt, 
Button4, 
B4, 
Double, 
Button5, 
B5 
Triple,
Mod1, 
M1. TYPE is one of 
Activate, 
Enter, 
Map,
ButtonPress, 
Button, 
Expose, 
Motion, 
ButtonRelease
FocusIn, MouseWheel, Circulate, FocusOut, Property,
Colormap, Gravity Reparent, Configure, KeyPress, Key,
Unmap, Deactivate, KeyRelease Visibility, Destroy,
Leave and DETAIL is the button number for ButtonPress,
ButtonRelease and DETAIL is the Keysym for KeyPress and
KeyRelease. Examples are
<Control-Button-1> for pressing Control and mouse button 1 or
<Alt-A> for pressing A and the Alt key (KeyPress can be omitted).
An event pattern can also be a virtual event of the form
<<AString>> where AString can be arbitrary. This
event can be generated by event_generate.
If events are concatenated they must appear shortly
after each other.

FUNC will be called if the event sequence occurs with an
instance of Event as argument. If the return value of FUNC is
"break" no further bound function is invoked.

An additional boolean parameter ADD specifies whether FUNC will
be called additionally to the other bound function or whether
it will replace the previous function.

Bind will return an identifier to allow deletion of the bound function with
unbind without memory leak.

If FUNC or SEQUENCE is omitted the bound function or list
of bound events are returned."""

zoomvalue = 1.2
underlay_zoom = 1.0
debug_move = 0
di = None
di_tk = None
def debug():
    global canvas,di,di_tk
    di = PIL.Image.new("RGBA", (g.width*g.col,g.height*g.row))
    for r in range(g.row):
        for c in range(g.col):
            PIL.ImageDraw.Draw(di).rectangle((g.width*r,g.height*c,g.width*(r+1),g.height*(c+1)),fill = (r,c,255,255),outline = (0,0,0,255))

    # PIL.ImageDraw.Draw(di).rectangle((0,0,1200,800),fill = (255,255,255,255,),outline = (0,0,0,255))
    di_tk = PIL.ImageTk.PhotoImage(di)
    canvas.create_image(0,0,image = di_tk,anchor = "nw")
def clear():
    canvas.delete("all")

x0 = 0
y0 = 0
x = 0
y = 0
sens = 1
# i = tk.PhotoImage()
# ii = PIL.ImageTk.PhotoImage()
def mouse_down(event):
    canvas.scan_mark(event.x,event.y)

def mouse_drag(event):
    canvas.scan_dragto(event.x, event.y, gain = 1)

def zoom_in(event):
    global zoomvalue,canvas
    # canvas.delete("all")
    zoomvalue_l = zoomvalue
    if event.delta > 0:
        zoomvalue_l = zoomvalue
    elif event.delta != 0:
        zoomvalue_l = 1/zoomvalue
    for p in g.stampbase_pi_tc.items():
        print(type(p[1]))
        zoomp = p[1].zoom(zoomvalue)
        g.stampbase_tc[p[0]] = zoomp
        g.stampbase_pi_tc[p[0]] = PIL.ImageTk.PhotoImage(zoomp)
    # m.draw_new_map()
    canvas.scale("all", 0,0,zoomvalue_l,zoomvalue_l)
    # for oid in canvas.find_all():
    #     if canvas.type(oid) == "image":
    #         i = canvas.itemcget(oid, "image")
    #         print(i)
    #         if event.delta > 0:
    #             i.zoom(zoomvalue)
    #         elif event.delta != 0:
    #             i.zoom(1/zoomvalue)
        # zoom = min(zoom + 0.5, 10)

        # zoom = max(zoom - 0.5,0.5)

def sort_layer():
    canvas.tag_raise("outline","all")
    canvas.tag_lower("terrain","all")

# new_hex_no = hide_new_hex

def new_hex_yes_th():
    pass
#### Definition for top level windows

def in_value_watchdog():
    pass



top = tk.Tk()
top.title("Canvas Test")
top.geometry("1366x400")

top.bind("<Configure>", onResizingMain)

g.make_new_stamp_base()

toolbar = tk.Canvas(top)
toolbar.grid(sticky = tk.W)

canvas = tk.Canvas(top, width = 1200, height = 700, xscrollincrement = 0, yscrollincrement = 0, scrollregion = (0,0,1200,800))
canvas.grid(column = 0, row = 1, sticky = tk.W)
# canvas.bind("<MouseWheel>",zoom_in)

circle = canvas.create_arc(50,50,100,100)

xsb = tk.Scrollbar(top, orient = tk.HORIZONTAL, command = canvas.xview)
ysb = tk.Scrollbar(top, command = canvas.yview)
canvas["xscrollcommand"] = xsb.set
canvas["yscrollcommand"] = ysb.set
xsb.grid(column = 0, row = 2, sticky = tk.W+tk.E)
ysb.grid(column = 1, row = 1, sticky = tk.N+tk.S)

bottomframe = tk.Frame(top)
debugbutton = tk.Button(bottomframe, text = "Debug", command = debug)
clearbutton = tk.Button(bottomframe, text = "Clear", command = clear)
zinbutton = tk.Button(bottomframe, text = "Zoom +", command = clear)
zoutbutton = tk.Button(bottomframe, text = "Zoom -", command = clear)
bottomframe.grid()
debugbutton.grid(column=0, row = 3)
zinbutton.grid(column=1, row = 3)
zoutbutton.grid(column=2, row = 3)

debugtextvar = tk.StringVar(value = "DEBUG")
debugLabel = tk.Label(top,textvariable = debugtextvar)
debugLabel.grid()
canvas.bind("<Button-1>", mouse_down)
canvas.bind("<Button1-Motion>",mouse_drag)

def onResizingMain(event):
    global canvas, top
    # if not g.initflag :
    #     g.initflag = True
    #     print("Initialized")
    w = top.winfo_width()
    h = top.winfo_height()
    canvas.config(width = w-100, height= h-100)
    x = canvas.winfo_width()
    y = canvas.winfo_height()
    # print("Resizing Main Window")