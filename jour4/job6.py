class Vehicule:
    def __init__(self,marque,annee,prix):
        self.marque = marque
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self):
        print("Marque :", self.marque)
        print("Année :",self.annee)
        print("Prix :",self.prix)

    def demarrer(self):
        return 'Attention je démarre'

class Voiture(Vehicule):
    def __init__(self, marque, annee, prix):
        super().__init__(marque, annee, prix)
        self.portes = 4

    def informationsVehicule(self):
        print("Marque :", self.marque)
        print("Année :",self.annee)
        print("Prix :",self.prix,"euros")
        print("Nombre de portes :", self.portes)

    def demarrer(self):
        return 'Attention je démarre ma voiture'

class Moto(Vehicule):

    def __init__(self, marque, annee, prix):
        super().__init__(marque, annee, prix)
        self.roues = 2

    def informationsVehicule(self):
        print("Marque :", self.marque)
        print("Année :",self.annee)
        print("Prix :",self.prix,"euros")
        print("Nombre de roues :", self.roues)

    def demarrer(self):
        return 'Attention je démarre ma moto'


  
    
car1 = Voiture("Honda","2012",10000)
moto1= Moto("BMW", "2023", 35000)

print(car1.informationsVehicule())
print(car1.demarrer())
print("-------------------------------")
print(moto1.informationsVehicule())
print(moto1.demarrer())


