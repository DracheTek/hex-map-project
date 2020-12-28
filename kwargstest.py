def test(**kwargs):
    if "fill" in kwargs:
        print(1)
    else:
        print(2)
        

def test2(**kwargs):
    # test(kwargs)
    pass

test(fill = "black", alpha = 0.1, outline = "white")