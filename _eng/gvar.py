import hexunit
from math import sqrt
initflag = False

STRING = type("str")
INT = type(0)
FLOAT = type(0.0)
DOUBLE = type(0.0)
TUPLE = type((0,))
LIST = type([0,])
DICT = type({"key" :"value"})
SQRT32 = sqrt(3)/2


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
    "red" : hexunit.HexUnit("red", "Red", (255,0,0)),
    "green" : hexunit.HexUnit("red", "Red", (255,0,0)),
    "blue" : hexunit.HexUnit("red", "Red", (255,0,0)),
    "black" : hexunit.HexUnit("red", "Red", (255,0,0)),
    "white" : hexunit.HexUnit("red", "Red", (255,0,0)),
}

for i in range(128):
    hexunitbase["white" + str(i)] = hexunit.HexUnit("white"+ str(i), "White "+str(i), (255,255,255)) 

## stamp base. Stores stamp (actual image) data in PIL pic form.
## tr = tc rotates 90deg. 
stampbase_tc = {}
stampbase_tr = {}

## thumbnail used for minimap.
## or reduce thumbnail and minimap to 4 pixels.

stampbase_tn_tc = {}
stampbase_tn_tr = {}

## stamp base in TK PhotoImage form. for future use.

stampbase_pi_tc = {}
stampbase_pi_tr = {}

## grid pic in PIL and TK form

grid_pil = None
grid_tk = None

## icon base for future use. 
## map. correspond x-y value for table. 