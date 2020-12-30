class HexUnit:
    name = "void"
    displayname = "Void"    #TODO: 本地化字符串
    color = (0,0,0) #transparent by default
    def __init__(self, name = "void", displayname = "Void", color = (0,0,0,)):
        self.name = name
        self.displayname = displayname
        self.color = color