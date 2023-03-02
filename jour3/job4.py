class Joueur:
    def __init__(self,nom,numero,position,buts,passes,carton_jaune,carton_rouge):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts = buts
        self.passes = passes
        self.carton_jaune = carton_jaune
        self.carton_rouge = carton_rouge

    def marquerUnBut(self):
        self.buts +=1

    def effectuerUnePasseDecisive(self):
        self.passes +=1

    def recevoirUnCartonJaune(self):
        self.carton_jaune +=1

    def recevoirUnCartonRouge(self):
        self.carton_rouge +=1

    def afficherStatistiques(self):
        print("Nom joueur :",self.nom)
        print("Numéro joueur :",self.numero)
        print("Position du joueur:",self.position)
        print("Nombre de buts :",self.buts)
        print("Nombres de passes décisives :", self.passes)
        print("Nombre de carton jaunes :",self.carton_jaune)
        print("Nombre de carton_rouge :",self.carton_rouge)

class Equipe:

    def __init__(self, nom):
        self.nom = nom
        self.joueurs = []

    def ajouterJoueur(self, joueur):
        self.joueurs.append(joueur)

    def afficherStatsJoueur(self):
        for joueur in self.joueurs:
            print(joueur.afficherStatistiques())

    def mettreAJourStatsJoueur(self, joueur,buts,passes,carton_jaune,carton_rouge):
        joueur.buts += buts
        joueur.passes += passes
        joueur.carton_rouge += carton_rouge
        joueur.carton_jaune += carton_jaune

equipe1 = Equipe("PSG")

joueur1 = Joueur("Messi", 10, "attaquant", 5, 0, 0, 0)
joueur2 = Joueur("Ronaldo", 3, "attaquant", 10, 0, 0, 0)
joueur3 = Joueur("Neymar", 16, "attaquant", 13, 0, 0, 0)
joueur4 = Joueur("De Bruyne", 12, "milieu", 4, 5, 0, 0)
joueur5 = Joueur("Xavi", 7, "milieu", 0, 9, 0, 0)
joueur6 = Joueur("Gavi", 19, "milieu", 0, 0, 0, 0)
joueur7 = Joueur("Renato", 10, "milieu", 0, 7, 0, 1)
joueur8 = Joueur("Mendes", 1, "defenseur", 0, 0, 0, 1)
joueur9 = Joueur("Ramos", 11, "defenseur", 0, 0, 2, 0)
joueur10 = Joueur("Militao", 23, "defenseur", 0, 10, 3, 0)
joueur11= Joueur("De Gea", 15, "gardien", 0, 0, 0, 0)


equipe2 = Equipe("OM")

joueur12 = Joueur("Vinicius", 99, "attaquant", 0, 0, 0, 0)
joueur13 = Joueur("Haaland", 98, "attaquant", 10, 0, 0, 0)
joueur14 = Joueur("Pedri", 97, "attaquant", 0, 0, 0, 0)
joueur15 = Joueur("Ruiz", 96, "milieu", 0, 0, 0, 0)
joueur16= Joueur("Kimmich", 95, "milieu", 0, 0, 0, 0)
joueur17 = Joueur("Goretzka", 94, "milieu", 0, 0, 0, 0)
joueur18 = Joueur("Mendy", 93, "defenseur", 0, 0, 0, 0)
joueur19= Joueur("Süle", 92, "defenseur", 0, 0, 0, 0)
joueur20= Joueur("Gigot", 91, "defenseur", 0, 0, 0, 0)
joueur21 = Joueur("Pavard", 90, "defenseur", 0, 0, 0, 0)
joueur22= Joueur("Ter Stegen", 89, "gardien", 0, 0, 0, 0)




equipe1.ajouterJoueur(joueur1)
equipe1.ajouterJoueur(joueur2)
equipe1.ajouterJoueur(joueur3)
equipe1.ajouterJoueur(joueur4)
equipe1.ajouterJoueur(joueur5)
equipe1.ajouterJoueur(joueur6)
equipe1.ajouterJoueur(joueur7)
equipe1.ajouterJoueur(joueur8)
equipe1.ajouterJoueur(joueur9)
equipe1.ajouterJoueur(joueur10)
equipe1.ajouterJoueur(joueur11)


equipe1.ajouterJoueur(joueur12)
equipe1.ajouterJoueur(joueur13)
equipe1.ajouterJoueur(joueur14)
equipe1.ajouterJoueur(joueur15)
equipe1.ajouterJoueur(joueur16)
equipe1.ajouterJoueur(joueur17)
equipe1.ajouterJoueur(joueur18)
equipe1.ajouterJoueur(joueur19)
equipe1.ajouterJoueur(joueur20)
equipe1.ajouterJoueur(joueur21)
equipe1.ajouterJoueur(joueur22)

joueur22.recevoirUnCartonJaune()
joueur3.recevoirUnCartonRouge()


equipe1.afficherStatsJoueur()

equipe1.mettreAJourStatsJoueur(joueur10, 1, 1, 1, 0)
equipe1.mettreAJourStatsJoueur(joueur19, 30, 1, 0, 0)
equipe1.mettreAJourStatsJoueur(joueur6, 1, 9, 2, 0)


equipe1.afficherStatsJoueur()