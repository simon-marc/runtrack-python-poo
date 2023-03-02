class Rectangle:
    def __init__(self,longueur,largeur):
        self.longueur = longueur
        self.largeur = largeur

    def perimetre (self):
        return 2*(self.longueur + self.largeur)

    def surface(self):
        return self.longueur * self.largeur

    def set_largeur(self,largeur):
        self.largeur = largeur

    def set_longueur(self,longueur):
        self.longueur = longueur

    def get_longueur(self):
        return self.longueur

    def get_largeur(self):
        return self.largueur

class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.hauteur = hauteur

    def set_hauteur(self, hauteur):
        self.hauteur = hauteur

    def get_hauteur(self):
        return self.hauteur 

    def volume(self):
        return self.surface() * self.hauteur

rectangle_1 = Rectangle(10,6)
print(rectangle_1.perimetre())
rectangle_1.set_largeur(11)
print(rectangle_1.surface())


para_1 = Parallelepipede(15,10,5)
print(para_1.volume())
print(para_1.set_hauteur(81))
print(para_1.volume())



