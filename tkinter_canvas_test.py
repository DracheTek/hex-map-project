from tkinter import *
from math import sqrt
from PIL import Image, ImageDraw, ImageTk


hexlist = []
images = []

SQRT3 = sqrt(3)

width = 40.0
height = 40.0
truerow = False
row = 16 #横行数
col = 40 #纵列数

def create_polygon_a(*args, **kwargs):  # alpha betwee 0~1
    if "alpha" in kwargs:
        if "fill" in kwargs:
            fill = top.winfo_rgb(kwargs.pop("fill"))\
                   + (int(kwargs.pop("alpha") * 255),)
            outline = kwargs.pop("outline") if "outline" in kwargs else None
            image = Image.new("RGBA", (int(max(args[::2])), int(max(args[1::2]))))
            ## 双冒号称为序列切片算符。
            ImageDraw.Draw(image).polygon(args,fill = fill, outline = outline)

            images.append(ImageTk.PhotoImage(image))
            return canvas.create_image(0,0,image=images[-1],anchor = "nw")
        raise ValueError("fill color must be specified")
    else:
        return canvas.create_polygon(*args, **kwargs)




def draw_line(start, end):
    pass

def draw_hex_tr(cv,**kwargs): #横方向上边相邻
    xs = [height*(3/4),height,height*(3/4),height*(1/4),0,height*(1/4)]
    ys = [0,width/2,width,width,width/2,0]
    for r in range(row):
        for c in range (col):
            id = cv.create_polygon(xs[0],ys[0],xs[1],ys[1],xs[2],ys[2],xs[3],ys[3],xs[4],ys[4],xs[5],ys[5])
            hexlist.__add__([id,])
            for i in range (len(xs)):
                xs[i] = xs[i] + width
        if (c % 2 == 0):
            xs = [width/2,width,width/2*3,width/2*3,width,width/2]
        else:
            xs = [0,width/2,width,width,width/2,0]
        for i in range(len(ys)):
            ys[i] = ys[i] + height/4*3   
    print(hexlist)
    pass

def draw_hex_tc(**kwargs): #竖直方向上边相邻
    if "fill" in kwargs:
        fill = kwargs.pop("fill")
    else:
        raise ValueError("fill color must be specified")
    alpha = kwargs.pop("alpha") if "alpha" in kwargs else 1
    outline = kwargs.pop("outline") if "outline" in kwargs else "black"
    xs = [width*(3/4),width,width*(3/4),width*(1/4),0,width*(1/4)]
    ys = [0,height/2,height,height,height/2,0]
    for c in range(col):
        for r in range(row):
            # cv.create_polygon(xs[0],ys[0],xs[1],ys[1],xs[2],ys[2],xs[3],ys[3],xs[4],ys[4],xs[5],ys[5],args)

            create_polygon_a(xs[0],ys[0],xs[1],ys[1],xs[2],ys[2],xs[3],ys[3],xs[4],ys[4],xs[5],ys[5],fill = "black", alpha = alpha,outline = outline)
            for i in range(len(ys)):
                ys[i] = ys[i] + height
        if (c % 2 == 0):
            ys = [height/2,height,height/2*3,height/2*3,height,height/2]
        else:
            ys = [0,height/2,height,height,height/2,0]
        for i in range(len(xs)):
            xs[i] = xs[i] + width/4*3     
    pass

top = Tk()
top.title("Canvas Test")
top.geometry("1366x768")

toolbutton = Menubutton(top, text = "Tool")
toolbutton.grid()
toolmenu = Menu(toolbutton, tearoff = 1)
toolbutton.menu = toolmenu
toolbutton['menu'] = toolmenu
toolmenu.add_command(label = "LINE")

# , scrollregion = (100,100,width*col*0.75+100,height*row+100)
canvas = Canvas(top, height = 700, width = 1300)
canvas.grid()



# filebutton = Menubutton(top, text = "File")
# filebutton.grid() #让控件显示在屏幕上。
# filemenu = Menu(filebutton ,tearoff = 0)
# filebutton.menu = filemenu
# filebutton['menu'] = filemenu



# c.create_line(0,0,100,173.2)# 0,0是窗口的左上角。向右向下为正
draw_hex_tc(fill = "black", alpha = 0.1, outline = "white")
# xs = [width*(3/4),width,width*(3/4),width*(1/4),0,width*(1/4)]
# ys = [0,height/2,height,height,height/2,0]
# create_polygon_a(xs[0],ys[0],xs[1],ys[1],xs[2],ys[2],xs[3],ys[3],xs[4],ys[4],xs[5],ys[5],fill = "black", alpha = 0.1)

top.mainloop()