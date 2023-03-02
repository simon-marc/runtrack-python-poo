class Personne:
    def __init__(self):
        self.age = 14
        
    def afficherAge(self):
        print(self.age)

    def bonjour(self):
        print("Hello")

    def modifierAge(self,newAge):
        self.age = newAge
        return self.age

class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")

    def affichageAge(self,age):
        self.age = age
        print("J'ai",self.age,"ans")


class Professeur:

    def __init__ (self, matiereEnseignee):
        self.matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print("Le cours va commencer")


pers = Personne()

eleve = Eleve()
eleve.affichageAge(14)




