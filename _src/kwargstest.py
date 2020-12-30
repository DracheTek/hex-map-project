width = 40
height = 40

row = 40
pattern1  = ()

for r in range(row):
    pattern1 = pattern1 + (width/4, r*height, 0, height*(r+1/2), width/4, height*(r+1))

print (pattern1)
print(list(pattern1))