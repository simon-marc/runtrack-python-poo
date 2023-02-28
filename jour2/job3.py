class Livre:
    def __init__(self, auteur,titre,pages,disponible):
        self.auteur = auteur
        self.titre = titre 
        self.pages = pages 
        self.disponible = disponible
    
    def changedAtt(self, auteur,titre,pages):
        if self.pages > 0:
            self.auteur = auteur
            self.titre = titre 
            self.pages = pages 
        else:
            print("Incorrect input")
        
    def display(self):
        print("Auteur :",self.auteur,"\n","Titre :",self.titre,"\n","Page numéro :", self.pages)

    def verification(self):
        if self.disponible:
            return "Livre disponible"
        else:
            return "Livre non disponible"

    def emprunter(self):
        if self.disponible:
            self.disponible = False
            return "Le livre a déjà été emprunté"
        else:
            return "Le livre disponible à l'emprunt"

    def rendre(self):
        if self.disponible:
            self.disponible = False
            return "Vous avez encore 3 jours pour rendre le livre emprunté"
        else:
            self.disponible = True
            return "Le livre emprunté a bien été rendu"





livre = Livre("LaPlateforme","yo",80,True)
print(livre.display())
livre.changedAtt("Neon", "Charles Baudelaire",200)
print(livre.display())
print(livre.emprunter())
print(livre.rendre())

