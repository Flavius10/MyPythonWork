from helpers.carte import Carte
from helpers.membru import Membru


class Gestiune:
    carti_imprumutate = {}

    def __init__(self):
        self.carti_disponibile = {}
        self.membri = {}

    def adauga_carte(self, titlu: str, autor: str, an: int):
        cartea = Carte(titlu, autor, an)
        self.carti_disponibile[cartea.titlu] = [cartea.autor, cartea.an]
        self.carti_imprumutate[cartea.titlu] = False
        print(f"Cartea cu titlul {cartea.titlu} a fost adaugata")

    def elemina_carte(self, titlu: str):
        cartea = Carte(titlu, "", 0)
        del self.carti_disponibile[cartea.titlu]
        print(f"Cartea {cartea.titlu} a fost stearsa")

    def inregistreaza_membru(self, nume: str, cod_membru: str):
        membrul = Membru(nume, cod_membru)
        self.membri[membrul.nume] = membrul.cod_membru
        print(f"Am adaugat membrul {membrul.nume}, cu {membrul.cod_membru} ca si cod")

    def sterge_membru(self, nume: str):
        membrul = Membru(nume, "")
        del self.membri[membrul.nume]
        print(f"Membrul {membrul.nume} a fost sters")

    def imprumuta_carte(self, titlu: str,  nume: str):
        cartea = Carte(titlu, "", 0)
        membrul = Membru(nume, "")
        self.carti_imprumutate[cartea.titlu] = True
        print(f"Ai imptumutat cartea {cartea.titlu} cu numele {membrul.nume}")

    def returneaza_carte(self, titlu):
        cartea = Carte(titlu, "", 0)
        print(f"Ai returnat cartea {cartea.titlu}")
        self.carti_imprumutate[cartea.titlu] = False

    def afiseaza_carti_disponibile(self):
        for cartea in self.carti_disponibile:
            if not self.carti_imprumutate[cartea]:
                print(f"Cartea {cartea} este disponibila")

    def afiseaza_membri(self):
        for membrul in self.membri:
            print(f"{membrul} este membru")

    def afiseaza_carti_imprumutate(self):
        for cartea in self.carti_imprumutate:
            if self.carti_imprumutate[cartea]:
                print(cartea)
