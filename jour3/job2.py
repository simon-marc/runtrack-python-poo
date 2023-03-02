class CompteBancaire :
    def __init__(self, nom, prenom, compte, solde, decouvert = True):
        self.nom = nom
        self.prenom = prenom
        self.compte= compte
        self.solde = solde
        self.decouvert = decouvert

    def afficher(self):
        print("Bonjour " ,self.nom , self.prenom,",","\n" "Vous êtes sur votre compte numéro : ", self.compte)

    def afficherSolde(self):
        print("Vous avez :",self.solde, "euros")

    def versement(self,somme):
        self.solde += somme

    def retrait(self, somme_retrait):
        if self.solde >= somme_retrait or self.decouvert:
            self.solde -= somme_retrait
            print("Vous avez effectué un retrait de :",somme_retrait, "euros")
        else: 
         return "Vous n'avez pas les fonds requis pour effectuer cette action !"

    def updateSolde(self):
        print("Votre nouveau solde est de : ",self.solde, "euros")

    def agios(self):
        if self.solde < 0 or self.decouvert:
            self.solde -= 10
            return "Vous êtes à découvert, des frais de dossier à hauteur de 10 euros vous ont été appliqués."

    def virement(self,personne, somme):
        if self.solde >= somme or self.decouvert:
            self.solde -= somme
            personne.versement(somme)
            print("Votre virement a bien effectué vers le compte :",self.compte)
        else : 
            return "Vous n'avez pas les fonds pour effectuer ce virement !"

        








personne1 = CompteBancaire("Anna","Borcheck", 230390292, 1000)
personne2 = CompteBancaire("James","Bakari",4002898219, -942)


personne2.afficher()
personne1.retrait(11)
personne1.retrait(89)
personne1.versement(10000)
personne2.updateSolde()

personne1.virement(personne2, 942)
personne2.afficher()
personne2.afficherSolde()
personne1.afficher()
personne1.afficherSolde()






