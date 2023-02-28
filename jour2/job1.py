class Rectangle:
    def __init__(self, longueur, largeur):
        self.largeur = largeur
        self.longueur = longueur

    def changedAtt(self, newLongueur, newLargeur):
        self.largeur = newLargeur
        self.longueur = newLongueur
    
    def display(self):
        print("La longueur du rectangle vaut :",self.longueur,"et sa longueur est de :",self.largeur)

rectangle = Rectangle(5,10)
print(rectangle.display())
rectangle.changedAtt(10,3)
print(rectangle.display())



