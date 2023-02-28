class Point:

    def __init__(self,y,x):
        self.x = x
        self.y = y

    def AfficherLesPoints(self):
        print((self.y, self.y))

    def AfficherX(self):
        print(self.x)

    def AfficherY(self):
        print(self.y)

    def ChangerX(self, new_valX):
        self.x = new_valX
    
    def ChangerY(self, new_valY):
        self.y = new_valY



