#din modulul X importam clasa Y

from datetime import date
from tabulate import tabulate


class Factura:
    seria = "Serie x"

    def __init__(self, numar: int, nume_produsa: str, cantitate: int, pret_buc: int):
        self.numar = numar
        self.nume_produsa = nume_produsa
        self.cantitate = cantitate
        self.pret_buc = pret_buc

    def schimba_cantitatea(self, cant: int):
        self.cantitate = cant

    def schimba_pretul(self, pret):
        self.pret_buc = pret

    def schimba_nume_produs(self, nume):
        self.nume_produsa = nume

    def genereaza_factura(self):
        print(f"Factura seria {self.seria} număr {self.numar}")
        print(f"Data: ", date.today())
        data1 = [["Produs", "Cantitate", "Pret Bucata", "Total"],
                 [self.nume_produsa, self.numar, self.pret_buc, self.pret_buc * self.numar]]

        table2 = tabulate(data1, headers='firstrow')

        print(table2)

