class Dreptunghi:
    def __init__(self, lungime: int, latime: int, culoare: str):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descrie(self):
        print(f"Dreptunghiul are lungimea de {self.lungime}, latimea de {self.latime}, iar culoarea {self.culoare}")

    def aria(self):
        return self.latime * self.lungime

    def perimetru(self):
        return self.latime * 2 + self.lungime * 2

    def schimbă_culoarea(self, noua_culoare: str):
        self.culoare = noua_culoare
