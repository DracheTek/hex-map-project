import hexunit

truecol = True
width = 48
height = 48
row = 4
col = 4
alpha = 255
hexpoint_tc = (
    0, height/2,
    width/4, 0,
    width*3/4, 0,
    width, height/2,
    width*3/4, height,
    width/4, height,
)

hexpoint_tr = (
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

## stamp base. Stores stamp (actual image) data 

stampbase_tc = {}

stampbase_tr = {}

## icon base for future use. 
## map. correspond x-y value for table. 