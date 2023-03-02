class Ville:
    def __init__(self, nom_ville,  nombre_habitant):
        self.nomVille = nom_ville
        self.nombreHab = nombre_habitant

    def incrVille(self):
      self.nombreHab += 1

    def dispVille(self):
        print("Population de la ville de ", self.nomVille ,":",self.nombreHab, "habitants")


class Personne:
    def __init__(self, nom , age , nom_ville):
        self.nomPers = nom_ville
        self.agePers = age
        self.nomVille = nom_ville

    def ajouterPopulation(self):
        self.nomVille.incrVille()





ville_1 = Ville("Paris", 1000000)
ville_2 = Ville("Marseille", 861635)

personne1 = Personne("John", 45, ville_1)
personne2 = Personne("Myrtille", 4, ville_1)
personne3 = Personne("Chloé", 18, ville_2)

print(ville_1.dispVille())
print(ville_2.dispVille())

personne1.ajouterPopulation()
personne2.ajouterPopulation()
personne3.ajouterPopulation()

print("Mise à jour de la population de Paris :", ville_1.dispVille())
print("Mise à jour de la population de Marseille :", ville_2.dispVille())





