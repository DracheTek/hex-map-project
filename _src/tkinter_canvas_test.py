from tkinter import *
from math import sqrt
from PIL import Image, ImageDraw, ImageTk


# hexlist = []
images = []

# SQRT3 = sqrt(3)

width = 40
height = 40
truerow = False
row = 16 #横行数
col = 80 #纵列数

xs1 = [height*(3/4),height,height*(3/4),height*(1/4),0,height*(1/4)]
ys1 = [0,width/2,width,width,width/2,0]


blackhex = None
redhex = None
greenhex = None
bluehex = None






def create_polygon_a(*args, **kwargs):  # alpha betwee 0~1
    if ("alpha" in kwargs) or (kwargs.get("alpha") == 1):
        fill = top.winfo_rgb(kwargs.pop("fill" if "fill" in kwargs else "black"))
        fill = fill + ((int(kwargs.pop("alpha")*255)),)
        outline = kwargs.pop("outline") if "outline" in kwargs else None
        image = Image.new("RGBA", (int(max(args[::2])), int(max(args[1::2]))))
        ## 双冒号称为序列切片算符。
        ImageDraw.Draw(image).polygon(args,fill = fill)

        images.append(ImageTk.PhotoImage(image)) # 这里占用了3G以上的内存。
        return canvas.create_image(0,0,image=images[-1],anchor = "nw")

        if "fill" in kwargs:
            fill = top.winfo_rgb(kwargs.pop("fill")) + (int(kwargs.pop("alpha") * 255),)
            # print(fill)
        raise ValueError("fill color must be specified") # replace by default value
    else:
        return canvas.create_polygon(*args, **kwargs)


def draw_hex_tr(**kwargs): #横方向上边相邻
    if "fill" in kwargs:
        fill = kwargs.pop("fill")
    else:
        raise ValueError("fill color must be specified")
    alpha = kwargs.pop("alpha") if "alpha" in kwargs else 1
    outline = kwargs.pop("outline") if "outline" in kwargs else "black"
    xs = [height*(3/4),height,height*(3/4),height*(1/4),0,height*(1/4)]
    ys = [0,width/2,width,width,width/2,0]
    for r in range(row):
        for c in range (col):
            create_polygon_a(xs[0],ys[0],xs[1],ys[1],xs[2],ys[2],xs[3],ys[3],xs[4],ys[4],xs[5],ys[5],fill = "black", alpha = alpha,outline = outline)
            # hexlist.__add__([id,])
            for i in range (len(xs)):
                xs[i] = xs[i] + width
        if (c % 2 == 0):
            xs = [width/2,width,width/2*3,width/2*3,width,width/2]
        else:
            xs = [0,width/2,width,width,width/2,0]
        for i in range(len(ys)):
            ys[i] = ys[i] + height/4*3
    pass

def draw_hex_tc(**kwargs): #竖直方向上边相邻
    if "fill" in kwargs:
        fill = kwargs.pop("fill")
    else:
        fill = "black"
        # raise ValueError("fill color must be specified")
    alpha = kwargs.pop("alpha") if "alpha" in kwargs else 1
    outline = kwargs.pop("outline") if "outline" in kwargs else "black"
    xs = [width*(3/4),width,width*(3/4),width*(1/4),0,width*(1/4)]
    ys = [0,height/2,height,height,height/2,0]
    for c in range(col):
        for r in range(row):
            # cv.create_polygon(xs[0],ys[0],xs[1],ys[1],xs[2],ys[2],xs[3],ys[3],xs[4],ys[4],xs[5],ys[5],args)

            create_polygon_a(xs[0],ys[0],xs[1],ys[1],xs[2],ys[2],xs[3],ys[3],xs[4],ys[4],xs[5],ys[5],fill = fill, alpha = alpha,outline = outline)
            for i in range(len(ys)):
                ys[i] = ys[i] + height
        if (c % 2 == 0):
            ys = [height/2,height,height/2*3,height/2*3,height,height/2]
        else:
            ys = [0,height/2,height,height,height/2,0]
        for i in range(len(xs)):
            xs[i] = xs[i] + width/4*3     
    pass

def draw_hex_tc_simp(**kwargs):
    xs = [width*(3/4),width,width*(3/4),width*(1/4),0,width*(1/4)]
    ys = [0,height/2,height,height,height/2,0]
    for c in range(col):
        for r in range (row):
            canvas.create_polygon(xs[0],ys[0],xs[1],ys[1],xs[2],ys[2],xs[3],ys[3],xs[4],ys[4],xs[5],ys[5],**kwargs)
            for i in range(6):
                ys[i] = ys[i] + height
        if (c % 2 == 0):
            ys = [height/2,height,height/2*3,height/2*3,height,height/2]
        else:
            ys = [0,height/2,height,height,height/2,0]
        for i in range(len(xs)):
            xs[i] = xs[i] + width/4*3     

def draw_hex_tc_stamp():
    x = width/2
    y = height/2
    for c in range(col):
        for r in range (row):
            # canvas.create_polygon(xs[0],ys[0],xs[1],ys[1],xs[2],ys[2],xs[3],ys[3],xs[4],ys[4],xs[5],ys[5],**kwargs)
            canvas.create_image(x,y,image=redhex,anchor = "nw")
            canvas.create_image(x,y,image = outlinehex, anchor = "nw")
            y = y + height
        if (c % 2 == 0):
            y = height
        else:
            y = height/2
        x = x + width*3/4


def onResizingMain(event):
    canvas.config(width = top.winfo_width(), height = top.winfo_height())
    # print("resized")


top = Tk()
top.title("Canvas Test")
top.geometry("640x480")

top.bind("<Configure>", onResizingMain)

toolbutton = Menubutton(top, text = "Tool")
toolbutton.grid()
toolmenu = Menu(toolbutton, tearoff = 1)
toolbutton.menu = toolmenu
toolbutton['menu'] = toolmenu
toolmenu.add_command(label = "LINE")

# , scrollregion = (100,100,width*col*0.75+100,height*row+100)
canvas = Canvas(top, height = 700, width = 1300)
canvas.grid()

imagebuffer = Image.new("RGBA",(width,height))
ImageDraw.Draw(imagebuffer).polygon((xs1[0],ys1[0],xs1[1],ys1[1],xs1[2],ys1[2],xs1[3],ys1[3],xs1[4],ys1[4],xs1[5],ys1[5],),fill = (0,0,0,255,))

blackhex = ImageTk.PhotoImage(imagebuffer)
imagebuffer = Image.new("RGBA",(width,height))
ImageDraw.Draw(imagebuffer).polygon((xs1[0],ys1[0],xs1[1],ys1[1],xs1[2],ys1[2],xs1[3],ys1[3],xs1[4],ys1[4],xs1[5],ys1[5],),fill = (255,0,0,255,))
redhex = ImageTk.PhotoImage(imagebuffer)
imagebuffer = Image.new("RGBA",(width,height))
ImageDraw.Draw(imagebuffer).polygon((xs1[0],ys1[0],xs1[1],ys1[1],xs1[2],ys1[2],xs1[3],ys1[3],xs1[4],ys1[4],xs1[5],ys1[5],),fill = (0,255,0,255,))
greenhex = ImageTk.PhotoImage(imagebuffer)
imagebuffer = Image.new("RGBA",(width,height))
ImageDraw.Draw(imagebuffer).polygon((xs1[0],ys1[0],xs1[1],ys1[1],xs1[2],ys1[2],xs1[3],ys1[3],xs1[4],ys1[4],xs1[5],ys1[5],),fill = (0,0,255,255,))
bluehex = ImageTk.PhotoImage(imagebuffer)
imagebuffer = Image.new("RGBA",(width,height))
ImageDraw.Draw(imagebuffer).polygon((xs1[0],ys1[0],xs1[1],ys1[1],xs1[2],ys1[2],xs1[3],ys1[3],xs1[4],ys1[4],xs1[5],ys1[5],),fill = (0,0,0,0,),outline = (0,0,0,255))
outlinehex = ImageTk.PhotoImage(imagebuffer)

# filebutton = Menubutton(top, text = "File")
# filebutton.grid() #让控件显示在屏幕上。
# filemenu = Menu(filebutton ,tearoff = 0)
# filebutton.menu = filemenu
# filebutton['menu'] = filemenu
# x = 0
# y = 0
# for r in range(row):
#     for c in range (col):
#         canvas.create_rectangle(x,y,x+width,y+height,fill = "black")
#         x = x+width
#     x = 0
#     y = y+height
# c.create_line(0,0,100,173.2)# 0,0是窗口的左上角。向右向下为正
# draw_hex_tc_simp(fill = "red", outline = "black")
draw_hex_tc_stamp()
#fill = "red", alpha = 0.1, outline = "white"
# draw_hex_tc(outline = "white")
# images.clear()
# xs = [width*(3/4),width,width*(3/4),width*(1/4),0,width*(1/4)]
# ys = [0,height/2,height,height,height/2,0]
# create_polygon_a(xs[0],ys[0],xs[1],ys[1],xs[2],ys[2],xs[3],ys[3],xs[4],ys[4],xs[5],ys[5],fill = "black", alpha = 0.1)

# while True:
#     top.update_idletasks() # 处理“闲时回调”
#     top.update() # 处理“事件”

top.mainloop()
