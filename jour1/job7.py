class Personnage:

    def __init__(self, x, y):
        self.y= y
        self.x = x

    def droite(self):
        self.x +=1

    def gauche(self):
        self.x -=1

    def bas(self):
        self.y +=1

    def haut(self):
        self.y -=1

    def position(self):
        return self.x, self.y

pos = Personnage(0,0)


print("Vous êtes à la position :",pos.position())
