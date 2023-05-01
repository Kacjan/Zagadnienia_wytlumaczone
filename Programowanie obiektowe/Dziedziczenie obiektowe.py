class Human:
    def __init__(self, name, height, weigth):
        self.name = name
        self.height = height
        self.weigth = weigth

    def krzycz(self):
        print("AAAAAAAAA!!!!!!!!!!!!!")


class Programist(Human):                                 # Żeby dziedziczenie działało:
    def __init__(self, name, height, weigth, languages): # Nazwy metod dziedziczonych musza być wpisane tutaj...
        super().__init__(name, height, weigth)           # i tutaj z funkcją super
        self.languages = languages


bob = Programist("Bob", 180, 100, ["Python", "Java"])
print(bob.name)  # Dostep do odziedziczonego po klasie Human pola name
bob.krzycz()
print(bob.height)