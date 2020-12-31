import hexunit

initflag = False

STRING = type("str")
INT = type(0)
FLOAT = type(0.0)
DOUBLE = type(0.0)
TUPLE = type((0,))
LIST = type([0,])
DICT = type({"key" :"value"})

truecol = True
width = 48
height = 48
row = 4
col = 4
alpha = 255

def hexpoint_tc():
    return (
    0, height/2,
    width/4, 0,
    width*3/4, 0,
    width, height/2,
    width*3/4, height,
    width/4, height,
    )

def hexpoint_tr():
    return (
    width/2,0,
    width, height/4,
    width, height*3/4,
    width/2, height,
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
stamplist_tc = []
stampbase_tc = {}

stampbase_tr = {}

## stamp base in TK PhotoImage form. for future use.

stampbase_pi_tc = {}
stampbase_pi_tr = {}

## icon base for future use. 
## map. correspond x-y value for table. 