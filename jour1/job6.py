class Animal:
    
    def __init__(self):
        self.age = 0
        self.prenom = ''

    def viellir(self):
        self.age = +1

    def nommer(self,prenom):
        self.prenom = prenom

animal = Animal()

print(f"L'age de l'animal", animal.age)
animal.viellir()
print(f"L'age de l'animal",animal.age)

animal.nommer("Simon")
print(f"L'animal se nomme",animal.prenom)
