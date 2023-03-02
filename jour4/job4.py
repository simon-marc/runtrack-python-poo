class Forme:
    def aire(self):
        return 0

class Rectangle(Forme):
    def __init__(self,largeur,hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
    
    def aire (self):
        return self.largeur * self.hauteur

rectangle_1 = Rectangle(6,16)

print(rectangle_1.aire())