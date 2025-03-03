class Angajat:
    def __init__(self, nume: str, prenume: str, salariu: int):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descrie(self):
        print(f"Numele meu este {self.nume} {self.prenume}, si am salariu de {self.salariu} Euro")

    def nume_complet(self):
        print(f"Numele meu este {self.nume} {self.prenume}")

    def salariu_lunar(self):
        return self.salariu

    def salariu_anual(self):
        return self.salariu * 10 + self.salariu * 3 * 2

    def marire_salariu(self, marire: int):
        return self.salariu + self.salariu * marire / 100

