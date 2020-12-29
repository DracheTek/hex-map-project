from tkinter import *
from PIL import Image, ImageDraw, ImageTk

GLOBAL_ALPHA = 255


width = 40
height = 40
xs1 = [width*(3/4),width,width*(3/4),width*(1/4),0,width*(1/4)]
ys1 = [0,height/2,height,height,height/2,0]
truerow = False
row = 40
col = 40

def draw_hex_stamp():
    if not truerow:
        x = width/2
        y = height/2
        for c in range(col):
            for r in range (row):
                # canvas.create_polygon(xs[0],ys[0],xs[1],ys[1],xs[2],ys[2],xs[3],ys[3],xs[4],ys[4],xs[5],ys[5],**kwargs)
                canvas.create_image(x,y,image=stampbase[2],anchor = "nw", tags = "stamp")
                canvas.create_image(x,y,image = outlinehex, anchor = "nw", tags = "outlinestamp")
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
                canvas.create_image(x,y,image = outlinehex, anchor = "nw", tags = "outlinestamp")
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


def onResizingMain(event):
    canvas.config(width = top.winfo_width(), height = top.winfo_height()-100)
    # print("resized")
# xs1 = [height*(3/4),height,height*(3/4),height*(1/4),0,height*(1/4)]
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
    print("Current Alpha:" + str(GLOBAL_ALPHA))




# make top level

top = Tk()
top.title("Canvas Test")
top.geometry("1366x768")

# bind resize event to top level

top.bind("<Configure>", onResizingMain)

# make tool buttons
filebutton = Menubutton(top, text = "File")
filebutton.grid(row = 0,column = 0,sticky = W)
toolbutton = Menubutton(top, text = "Tool")
toolbutton.grid(row = 0,column = 1,sticky = W)
toolmenu = Menu(toolbutton, tearoff = 1)
toolbutton.menu = toolmenu
toolbutton['menu'] = toolmenu
toolmenu.add_command(label = "LINE")


# make canvas

canvas = Canvas(top, height = 700, width = 1300)
canvas.grid(row = 1, column = 1,pady = 50)
# make buttons

button_alphaup = Button(top, text= "Alpha +", command = increaseAlpha)
button_alphaup.grid()

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
imagebuffer = Image.new("RGBA",(width,height))
ImageDraw.Draw(imagebuffer).polygon((xs1[0],ys1[0],xs1[1],ys1[1],xs1[2],ys1[2],xs1[3],ys1[3],xs1[4],ys1[4],xs1[5],ys1[5],),fill = (0,0,0,0,),outline = (0,0,0,255))
outlinehex = ImageTk.PhotoImage(imagebuffer)

del xs1
del ys1

underlay = Image.new("RGBA",(500,500))

draw_hex_stamp()
# draw_base_map()

top.mainloop()