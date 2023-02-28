class Personne:
    def __init__(self, name, lastname):
        self.lastname = lastname
        self.name = name

    def SePresenter(self):
        print("Je suis", self.name, self.lastname)


example1 = Personne("Simon", "Marc")
example2 = Personne("Lucas","Lombardo")
example3 = Personne("Mathieu","Tan")

print(example1.SePresenter())
print(example2.SePresenter())
print(example3.SePresenter())