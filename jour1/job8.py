import math

class Cercle:
    def __init__(self,rayon):
        self.rayon = rayon

    def changerRayon(self, newRayon):
        self.rayon = newRayon

    def circonférence(self):
        return 2*math.pi*self.rayon

    def aire(self):
        return math.pi * self.rayon**2

    def diametre(self):
        return self.rayon*2

    def afficherInfos(self):
        print("Le rayon vaut :", self.rayon, "La circonférence vaut :", self.circonférence(), "Le diamètre vaut :", self.diametre(), "L'aire vaut :", self.diametre())

cercle_1 = Cercle(4)
cercle_2 = Cercle(7)

cercle_1.afficherInfos()
cercle_2.afficherInfos()