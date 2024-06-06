class Tile:
    
    def __init__(self, x, y, status):
        self.row = x
        self.col =  y
        self.status = status
        self.value = 0

    def show(self):
        print ("row", self.row, "col", self.col, "valu", self.value )