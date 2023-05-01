class Human:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

class Animal:
    def __init__(self, legs):
        self.legs = legs

class Programmer(Human, Animal):
    def __init__(self, name, height, weight, legs, languages):
        super().__init__(name, height, weight)
        Animal.__init__(self, legs)
        self.languages = languages