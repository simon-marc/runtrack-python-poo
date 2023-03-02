class Forme:
    def aire(self):
        return 0

class Cercle(Forme):
    def __init__(self,radius):
        self.radius = radius

    def aire (self):
        return 3.14*self.radius**2

class Rectangle(Forme):
    def __init__(self,largeur,hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
         
    def aire (self):
        return self.largeur * self.hauteur


cercle1 = Cercle(20)
rectangle1= Rectangle(10,19)
print(cercle1.aire())
print(rectangle1.aire())