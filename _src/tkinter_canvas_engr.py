from tkinter import *
from PIL import Image, ImageDraw, ImageTk

GLOBAL_ALPHA = 255


width = 48
height = 48
xs1 = [width*(3/4),width,width*(3/4),width*(1/4),0,width*(1/4)]
ys1 = [0,height/2,height,height,height/2,0]
truerow = False
row = 40
col = 40

overlayimage = None

def draw_hex_stamp():
    if not truerow:
        x = width/2
        y = height/2
        for c in range(col):
            for r in range (row):
                # canvas.create_polygon(xs[0],ys[0],xs[1],ys[1],xs[2],ys[2],xs[3],ys[3],xs[4],ys[4],xs[5],ys[5],**kwargs)
                canvas.create_image(x,y,image=stampbase[2],anchor = "nw", tags = "stamp")
                # canvas.create_image(x,y,image = outlinehex, anchor = "nw", tags = "outlinestamp")
                y = y + height
            if (c % 2 == 0):
                y = height
            else:
                y = height/2
            x = x + width*3/4
    else:
        y = height/2
        x = width /2

        for r in range (row):
            for c in range (col):
                canvas.create_image(x,y,image=stampbase[2],anchor = "nw", tags = "stamp")
                # canvas.create_image(x,y,image = outlinehex, anchor = "nw", tags = "outlinestamp")
                x = x+width
            if (r%2 == 0):
                x = width
            else :
                x = width /2
            y = y + width * 3 / 4

def draw_base_map():
    # underlay = Image.open("battlefield_overview.png")
    global underlay
    underlay = Image.new("RGBA",(100,100))
    underlay = Image.open("battlefield_overview.png")
    underlay = ImageTk.PhotoImage(underlay)
    canvas.create_image(300,300,image = underlay, anchor = "nw")

def draw_hex_grid():
    pass

def onResizingMain(event):
    canvas.config(width = top.winfo_width(), height = top.winfo_height()-300)
    # print("resized")
# xs1 = [height*(3/4),height,height*(3/4),height*(1/4),0,height*(1/4)]

def onInit():
    global overlayimage
    print("Init")
    draw_hex_stamp()
    overlayimage = canvas.create_image(width/2,height/2,image = outlinehex, anchor = "nw", state = NORMAL) # id
    draw_base_map()

def increaseAlpha():
    global GLOBAL_ALPHA 
    global xs1 
    global ys1
    global width 
    global height
    i = 0
    GLOBAL_ALPHA = GLOBAL_ALPHA + 16
    if(GLOBAL_ALPHA > 255):
        GLOBAL_ALPHA = 0
    for colors in colorbase:
        imagebuffer = Image.new("RGBA",(width,height))
        ImageDraw.Draw(imagebuffer).polygon((width*(3/4),0,width,height/2,width*(3/4),height,width*(1/4),height,0,height/2,width*(1/4),0,),fill = colors + (GLOBAL_ALPHA,))
        stampbase[i] = ImageTk.PhotoImage(imagebuffer)
        i = i + 1
    canvas.delete("stamp")
    canvas.delete("outlinestamp")
    draw_hex_stamp()
    canvas.tag_raise(overlayimage)
    print("Current Alpha:" + str(GLOBAL_ALPHA))

def toggle_overlay():
    # canvas.itemconfigure(overlayimage, state = HIDDEN)
    state = canvas.itemcget(overlayimage, "state")
    # print (state)
    if (state == HIDDEN):
        canvas.itemconfigure(overlayimage, state = NORMAL)
    elif (state == NORMAL):
        canvas.itemconfigure(overlayimage, state = HIDDEN)


# make top level

top = Tk()
top.title("Canvas Test")
top.geometry("1366x768")

# bind resize event to top level

top.bind("<Configure>", onResizingMain)
top.bind("<Activate>", onInit)

# make tool bar

toolbar = Canvas (top)
toolbar.grid(sticky = W)

# make tool buttons

filebutton = Menubutton(toolbar, text = "File")
filebutton.grid(row = 0,column = 0,sticky = W)
toolbutton = Menubutton(toolbar, text = "Tool")
toolbutton.grid(row = 0,column = 1,sticky = W)
toolmenu = Menu(toolbutton, tearoff = 1)
toolbutton.menu = toolmenu
toolbutton['menu'] = toolmenu
toolmenu.add_command(label = "LINE")


# make canvas

canvas = Canvas(top, height = 700, width = 1300)
canvas.grid(row = 1,pady = 50)
# make buttons

button_alphaup = Button(top,text= "Alpha +", command = increaseAlpha)
button_alphaup.grid( sticky = W)
button_togglegrid = Button (top,  text = "Toggle Grid", command = toggle_overlay)
button_togglegrid.grid(sticky = W)
button_Init = Button (top,  text = "Init", command = onInit)
button_Init.grid()
# make stamps

blackhex = PhotoImage()
redhex = PhotoImage()
greenhex = PhotoImage()
bluehex = PhotoImage()

stampbase = []
colorbase = [
    (0,0,0),
    (255,0,0),
    (0,255,0),
    (0,0,255),
]

colorindex = 0
imagebuffer = None
for colors in colorbase:
    imagebuffer = Image.new("RGBA",(width,height))
    ImageDraw.Draw(imagebuffer).polygon((xs1[0],ys1[0],xs1[1],ys1[1],xs1[2],ys1[2],xs1[3],ys1[3],xs1[4],ys1[4],xs1[5],ys1[5],),fill = colors + (GLOBAL_ALPHA,))
    stampbase.append(ImageTk.PhotoImage(imagebuffer))
    # colorindex = colorindex + 1

# imagebuffer = Image.new("RGBA",(width,height))
# ImageDraw.Draw(imagebuffer).polygon((xs1[0],ys1[0],xs1[1],ys1[1],xs1[2],ys1[2],xs1[3],ys1[3],xs1[4],ys1[4],xs1[5],ys1[5],),fill = (0,0,0,255,))
# blackhex = ImageTk.PhotoImage(imagebuffer)
# imagebuffer = Image.new("RGBA",(width,height))
# ImageDraw.Draw(imagebuffer).polygon((xs1[0],ys1[0],xs1[1],ys1[1],xs1[2],ys1[2],xs1[3],ys1[3],xs1[4],ys1[4],xs1[5],ys1[5],),fill = (255,0,0,255,))
# redhex = ImageTk.PhotoImage(imagebuffer)
# imagebuffer = Image.new("RGBA",(width,height))
# ImageDraw.Draw(imagebuffer).polygon((xs1[0],ys1[0],xs1[1],ys1[1],xs1[2],ys1[2],xs1[3],ys1[3],xs1[4],ys1[4],xs1[5],ys1[5],),fill = (0,255,0,255,))
# greenhex = ImageTk.PhotoImage(imagebuffer)
# imagebuffer = Image.new("RGBA",(width,height))
# ImageDraw.Draw(imagebuffer).polygon((xs1[0],ys1[0],xs1[1],ys1[1],xs1[2],ys1[2],xs1[3],ys1[3],xs1[4],ys1[4],xs1[5],ys1[5],),fill = (0,0,255,255,))
# bluehex = ImageTk.PhotoImage(imagebuffer)

# make hex grid overlay

# this procedure takes 50s on average computer

# imagebuffer = Image.new("RGBA",(int(width * col* 3 / 4+width / 4) , int(height * row + height/2)))
# x = 0
# y = 0
# for c in range(col):
#     for r in range(row):
#         ImageDraw.Draw(imagebuffer).polygon((x+xs1[0],y+ys1[0],x+xs1[1],y+ys1[1],x+xs1[2],y+ys1[2],x+xs1[3],y+ys1[3],x+xs1[4],y+ys1[4],x+xs1[5],y+ys1[5],),fill = (0,0,0,0,),outline = (0,0,0) + (GLOBAL_ALPHA,))
#         y = y + height
#     if (c % 2 ==1):
#         y = 0
#     else:
#         y = height/2
#     x = x + width/4*3
# outlinehex = ImageTk.PhotoImage(imagebuffer)

imagebuffer = Image.new("RGBA",(int(width*col*3/4+width/4)+10, int(height*row+height/2)+10,))

pattern1 = []
toppattern = []
botpattern = []
for c in range (col+1):
    # print(c)
    if (c%2==0):
        toppattern.append((width*(c*3/4),height/2,))
        if (c != col):
            toppattern.append((width*(c*3/4+1/4),0,))
            botpattern.append((width*(c*3/4+3/4),height*row,))
            botpattern.append((width*(c*3/4+1),height*(row+1/2),))

        for r in range(row):
            pattern1.append((width*(c*3/4),height*(r+1/2),))
            pattern1.append((width*(c*3/4+1/4), height*(r+1),))
        pattern1.append((width*(c*3/4+1/4),height*(row),))
        if(c!=col):
            pattern1.append((width*(c*3/4+3/4),height*(row),))
    else:
        toppattern.append((width*(c*3/4),0,))
        if (c != col):
            toppattern.append((width*(c*3/4+1/4), height/2,))
            botpattern.append((width*(c*3/4+3/4),height*(row+1/2),))
            botpattern.append((width*(c*3/4+1),height*(row),))

        for r in range(row-1,0,-1):
            pattern1.append((width*(c*3/4+1/4),height*(r+1/2),))
            pattern1.append((width*(c*3/4),height*(r),))
        pattern1.append((width*(c*3/4+1/4),height/2,))
        # pattern1.append((width*(c+1/2),height/2))

# ImageDraw.Draw(imagebuffer).line(pattern1,fill = (0,0,0,255), width = 3)
# ImageDraw.Draw(imagebuffer).line(toppattern, fill = (0,0,0,255), width = 3)
# ImageDraw.Draw(imagebuffer).line(botpattern, fill = (0,0,0,255), width = 3)

for c in range (col):
    y = 1 if (c%2==0) else 3/2
    x = c*3/4+1/4
    for r in range (row-1):
        pass
        # ImageDraw.Draw(imagebuffer).line([x*width,(y+r)*height,x*width+width*1/2,(y+r)*height], fill = (0,0,0,255), width = 3)

outlinehex = ImageTk.PhotoImage(imagebuffer)


# x = 0
# y = 0
# pattern1 = ()
# pattern2 = []
# for r in range (row):
#     pattern1 = pattern1 + (width/4, r*height, 0, height*(r+1/2), width/4, height*(r+1))
# pattern2 = list(pattern1)
# for c in range (col):
#     ImageDraw.Draw(imagebuffer).line(list(pattern1), fill = (0,0,0), width = 2)






underlay = Image.new("RGBA",(500,500))
overlayimage = canvas.create_line(0,0,1,1)
# draw_hex_stamp()
# overlayimage = canvas.create_image(width/2,height/2,image = outlinehex, anchor = "nw", state = NORMAL) # id
# draw_base_map()

top.mainloop()
