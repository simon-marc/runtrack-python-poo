class Student:
    def __init__(self,nom,prenom,numb_etudiant,numb_credits):
        self.nom = nom 
        self.prenom = prenom
        self.etudiant = numb_etudiant
        self.credit = numb_credits
        self.level = self.studentEval

    def add_credit(self, credit):
        if self.credit > 0 and type(self.credit)==int:
            self.credit += credit
        else:
            return "Incorrect input"

    def studentEval(self):
        if self.credit >= 90:
            return "Excellent"
        if self.credit >= 80:
            return "Très bien"
        if self.credit >= 70:
            return "Bien"
        if self.credit >= 60:
            return "Passable" 
        if self.credit < 60:
            return "Insuffisant"        

    def studentInfo(self):
        print(" Nom = ", self.nom ,"\n","Prénom = ", self.prenom,"\n", "id = ",self.etudiant,"\n","Points = ", self.credit,"\n","Niveau = ", self.level())


eleve = Student("Joe", "Don",145,20)
eleve.add_credit(50)
eleve.add_credit(-10)
print(eleve.studentInfo())
