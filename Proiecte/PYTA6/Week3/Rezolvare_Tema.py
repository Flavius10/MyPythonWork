"""Exercitiul 1"""

# from Week3 import Cerc
# from Cerc import Cerc
#
# cerc = Cerc(10, "Rosu")
# cerc.descrie_cerc()
# print(cerc.aria())
# print(cerc.diametru())
# print(cerc.circumferinta())

"""Exercitiul 2"""

# from Week3 import Dreptunghi
# from Dreptunghi import Dreptunghi
#
# dreptunghi = Dreptunghi(10, 20, "Albastru")
# dreptunghi.descrie()
# print(dreptunghi.aria())
# print(dreptunghi.perimetru())
# dreptunghi.schimbă_culoarea("Verde")
# dreptunghi.descrie()

"""Exercitiul 3"""

# from Week3 import Angajat
# from Angajat import Angajat
#
# angajat = Angajat("Alexa", "Flavius Catalin", 10000)
# angajat.descrie()
# angajat.nume_complet()
# print(angajat.salariu_lunar())
# print(angajat.salariu_anual())
# print(angajat.marire_salariu(20))

"""Exercitiul 4"""

# from Week3 import Cont
# from Cont import Cont
#
# cont = Cont("iban", "Flavius", 1000000)
# cont.afisare_sold()
# print(cont.debitare_cont(40000))
# print(cont.creditare_cont(10))

"""Exercitiul 5"""

#din folderul X importam fisierul Y
from Week3 import Factură

#din fisierul X importam clasa Y
from Factură import Factura

factura = Factura(10, "Telefon", 20, 5000)

factura.genereaza_factura()
