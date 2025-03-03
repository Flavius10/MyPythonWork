"""
Programarea Orientată pe Obiecte

O paradigmă de programare reprezintă un set de principii și stiluri de a aborda
și rezolva problemele de programare. Ea definește modul în care sunt organizate
și structurate instrucțiunile și datele într-un program.

În Python există mai multe paradigme, dar cele mai uzuale sunt:
  1. Procedurală: programul este structurat în instrucțiuni secvențiale;
  2. Orientată pe Obiecte (OOP): programul este structurat în jurul obiectelor
  care încapsulează datele și comportamentele. Se bazează pe conceptele de clase
  obiecte și metode.

O clasă reprezintă o structură care definește caracteristicile și comportamentul
unui obiect. Poate conține variabile numite atribute (proprietăți) și funcții
numite metode. Clasele sunt utilizate ca șabloane/schițe pentru a crea obiecte.

Un obiect este implementarea concretă (instanță) a unei clase. Se bazează pe
definiția și comportamentul specificate de clasă.
Ex. o clasă „Masina” poate fi utilizata pentru a crea mai multe obiecte de tip
mașină, fiecare având propriile sale atribute și metode.

O clasă conține proprietăți (atribute) și metode.
O proprietate este o variabilă definită în clasă, care reprezintă o caracteristică
a unui obiect creat pe baza clasei respective.
Ex. Clasa „Masina” poate avea proprietăți precum „marca”, „model”, „an”, „culoare” etc.
Metodele sunt funcții definite într-o clasă și sunt folosite pentru a defini
comportamentul obiectelor. Acestea pot accesa și manipula proprietățile obiectului.
Ex. Clasa „Masina” poate avea metode precum „accelereaza” sau „franeaza”.

Constructorul este o metodă specială definită într-o clasă și este utilizată
pentru a inițializa obiectele din acea clasă. Este denumit '__init__()' și
este apelat automat la crearea unui obiect nou. Acesta poate primi parametri
pentru a inițializa atributele obiectului.
"""
class Masina:
    # Constructor / Dunder method, metodă specială
    def __init__(self, marca: str, model: str, an: int, culoare: str):
        self.marca = marca
        self.model = model
        self.an = an
        self.culoare = culoare
        self.motor_pornit = False
        self.viteza_curenta = 0

    def some_method(self):
        # if not:
        #     return actiune_negativa
        #
        # return actiune_pozitiva
        ...

    def porneste_motor(self, ):
        if self.motor_pornit:
            return "Motorul este deja pornit."

        self.motor_pornit = True
        return "Motorul a fost pornit."

    def opreste_motor(self):
        if self.motor_pornit:
            self.motor_pornit = False
            self.viteza_curenta = 0
            return "Motorul a fost oprit."

        return "Motorul este deja oprit."

    # Putem adăuga parametri suplimentari
    def accelereaza(self, viteza):
        if not self.motor_pornit:
            return "Motorul trebuie să fie pornit pentru a accelera."

        self.viteza_curenta += viteza  # self.viteza_curenta = self.viteza_curenta + viteza
        return f"Mașina a accelerat la viteza de {self.viteza_curenta} km/h."

    def franeaza(self, viteza):
        if self.viteza_curenta >= viteza:
            self.viteza_curenta -= viteza
            return f"Mașina a frânat la viteza de {self.viteza_curenta} km/h."

        return "Viteza curentă nu poate fi mai mică decât viteza de frânare."



# Inițializare / Instanțiere a clasei
# Obiecte
toyota = Masina("Toyota", "Corolla", 2022, "vișinie")
ford = Masina("Ford", "Mustang", 2019, "neagră")
audi = Masina("Audi", "A4", 2018, "gri")
dacia = Masina("Dacia", "Logan", 2009, "albă")

# O proprietate / metodă poate fi accesată în următorul mod:
# print(f"Mașina mea este o {toyota.marca} {toyota.model}, din anul {toyota.an}, de culoarea {toyota.culoare}.")
print("Toyota are motorul pornit?", toyota.motor_pornit)
print("-"*20)
print(toyota.porneste_motor())
print("-"*20)
print("Toyota are motorul pornit?", toyota.motor_pornit)
print("-"*20)
print(toyota.accelereaza(30))
print("-"*20)
print(toyota.accelereaza(50))
print("-"*20)
print(toyota.accelereaza(30))
print("-"*20)
print(toyota.franeaza(60))
print(toyota.franeaza(50))
print("-"*20)
print(toyota.opreste_motor())

# Metode Python built-in
# print()
# type()
