class Livre:
    def __init__(self, auteur,titre,pages):
        self.auteur = auteur
        self.titre = titre 
        self.pages = pages 
    
    def changedAtt(self, auteur,titre,pages):
        if self.pages > 0:
            self.auteur = auteur
            self.titre = titre 
            self.pages = pages 
        else:
            print("Incorrect input")
        
    def display(self):
        print("Auteur :",self.auteur,"\n","Titre :",self.titre,"\n","Page numéro :", self.pages)

livre = Livre("LaPlateforme","yo",80)
print(livre.display())
livre.changedAtt("Neon", "Charles Baudelaire",200)
print(livre.display())


