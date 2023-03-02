
class Tache:
    def __init__(self,titre,description):
        self.titre = titre
        self.description = description
        self.statut = "A faire"

class ListeDeTache:
        def __init__(self):
            self.taches = []

        def ajouterTache(self, tache):
            if tache not in self.taches:
                self.taches.append(tache)
            else:
                return "Tâche déja existante"

        def afficherListe(self):
            for tache in self.taches:
                print(f"Titre : {tache.titre} \ Description : {tache.description} \ Statut : {tache.statut}")

        def supprimerTache(self,tache):
            if tache in self.taches:
                self.taches.remove(tache)
            else:
                return "Tâche inexistante"

        def marquerCommeFinie(self,tache):
            tache.statut = "Terminé"

        def filtrerListe(self, statut):
            for tache in self.taches:
                if tache.statut == statut:
                    print(f" Titre : {tache.titre} \ Description : {tache.description} \ Statut : {tache.statut}")


liste = ListeDeTache()

tache_1 = Tache("edf","payer facture")
tache_2 = Tache("voiture","vidange")
tache_3 = Tache("shopping","corteiz")

liste.ajouterTache(tache_3)
liste.marquerCommeFinie(tache_3)
liste.ajouterTache(tache_2)
liste.filtrerListe("Terminé")








