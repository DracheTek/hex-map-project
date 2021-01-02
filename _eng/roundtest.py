from math import sqrt,floor,ceil
from PIL import ImageDraw
import threading 
from time import sleep
import mythread
import matplotlib.colors as c

stringtoread = """water,Water,#0099ff
deepwater,Deep Water,#0066cc
ocean,Ocean,#0000FF
deepocean,Deep Ocean,#000066
southevergreen,Evergreen Forest (Broad Leaf),#006600
northevergreen,Evergreen Forest (Coniferous),#003333
mixedforest,Mixed Forest,#009900
tropicaljungle,Tropical Jungle,#003300
grassland,Grass Land,#66ff00
farmland,Farm Land,#99ff00
builtup,Bulit Up Area,#808080
builtupdense,Bulit Up Area(Dense),#2f2f2f
"""
lines = stringtoread.split("\n")[0:-2:1]
for l in lines:
    words = l.split(",")
    name = words[0]
    displayname = words[1]
    colorstring = words[2]
    r = int(colorstring[1:3:],16)
    g = int(colorstring[3:5:],16)
    b = int(colorstring[5:7:],16)
    print('"%s":hexunit.HexUnit("%s","%s",(%d,%d,%d)),'%(name,name,displayname,r,g,b))