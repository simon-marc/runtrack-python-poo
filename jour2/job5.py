class Voiture:
    def __init__(self, brand, model,year,mileage,tank = 50, en_marche=False):
        self.brand = brand
        self.model = model 
        self.year = year
        self.numb_km = mileage
        self.reservoir = tank
        self.en_marche = en_marche

    def demarrer(self):
        if self.reservoir > 5:
            self.en_marche = True
            return "Car is able to be started"
        else:
            return "Car hasn't enough gas for starting"
        
    def arreter(self):
        if self.en_marche:
            self.en_marche = False
            return "Car is stopped"

    def verifier_reservoir(self):
        print("Your tank contains",self.reservoir, "L")


car = Voiture("Nissan","GT-R",2010,49832)
print(car.demarrer())
print(car.arreter())
print(car.verifier_reservoir())







