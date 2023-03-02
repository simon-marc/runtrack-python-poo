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

    def affichageAge(self):
        print("J'ai",self.age,"ans")


class Professeur(Personne):

    def __init__ (self, matiereEnseignee):
        self.matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print("Aujourd'hui le cours va porter sur le matière : ",self.matiereEnseignee)




eleve = Eleve()
eleve.bonjour()
eleve.allerEnCours()
eleve.modifierAge(15)
eleve.affichageAge()

professeur = Professeur("Sciences et Vie de la Terre")
professeur.bonjour()
professeur.modifierAge(40)
professeur.enseigner()





