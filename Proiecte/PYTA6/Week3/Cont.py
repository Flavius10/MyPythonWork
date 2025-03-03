class Cont:
    def __init__(self, iban: str, titular_cont: str, sold: float):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self):
        print(f"Titularul {self.titular_cont} are în contul {self.iban} suma de {self.sold} lei")

    def debitare_cont(self, suma: int):
        self.sold += suma
        return self.sold

    def creditare_cont(self, suma: int):
        self.sold -= suma
        return self.sold

