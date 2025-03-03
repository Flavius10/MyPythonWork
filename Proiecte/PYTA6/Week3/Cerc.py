import math


class Cerc:

    def __init__(self, raza: int, culoare: str):
        self.raza = raza
        self.culoare = culoare

    def descrie_cerc(self):
        print(f"Cercul are raza egala cu {self.raza} si culoarea {self.culoare}")

    def aria(self):
        return math.pi * self.raza * self.raza

    def diametru(self):
        return self.raza * 2

    def circumferinta(self):
        return math.pi * 2 * self.raza
