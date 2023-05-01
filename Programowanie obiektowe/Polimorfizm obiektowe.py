from typing import List

class Figura:
    def __init__(self):
        pass

    def pole_powierzchni(self):
        pass


class Trojkat(Figura):
    def __init__(self, h, a):
        super().__init__()
        self.h = h
        self.a = a

    def pole_powierzchni(self):
        return f"Trojkat ma pole: {(self.a * self.h) / 2}"


class Kwadrat(Figura):
    def __init__(self, a):
        super().__init__()
        self.a = a

    def pole_powierzchni(self):
        return f"Kwadrat ma pole: {self.a * self.a}"


lista_figur: List[Figura] = [Kwadrat(2), Trojkat(10, 20), Kwadrat(50)]

for figura in lista_figur:
    print(figura.pole_powierzchni())