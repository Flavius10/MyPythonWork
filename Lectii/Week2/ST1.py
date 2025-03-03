"""
Topicul principal: Colecții de date în Python
    1. Liste;
    2. Tupluri;
    3. Seturi;
    4. Dicționare.
"""
# 1. Liste - sintaxa este cu paranteză pătrată - []
# Listele sunt colecții de date ordonate, ele putând fi accesate după index-ul corespunzător fiecărui element;
# Dacă încercăm să accesăm index care nu corespunde dimensiunii listei, codul va genera o eroare
# Lista este o colecţie da date mutabilă, adică putem schimba, şterge, sau adăuga elemente
# Castul se face cu „list()”
nume = ["Alin", "George", "Constantin", "Bianca"]
# print(nume)
# print(nume[0])
# print(nume[1:3])
# print(nume[2])
# print(nume[3])
# print(nume[4]) - va genera o eroare

nume.append("Radu") # metodă specială pentru a adăuga un element într-o listă; element se adaugă by default la final

nume.insert(2, "Ion") # inserează un element nou la un index specific

nume[0] = "Felix" # modalitate de a schimba un element

nume.pop(1) # metodă specială pentru a șterge un element

nume.append("Felix") # permite elemente duplicate
# print(nume)
# print(len(nume)) # printează lungimea listei


# 2. Tupluri
# Sintaxa este cu paranteză rotundă - ()
# Castul se face cu „tuple()”
colegi = ("Alin", "George", "Constantin", "Bianca")
print(colegi[0])
print(len(colegi))
# colegi[0] = "Felix" # va genera o eroare

# 3. Seturi
# Sintaxa este cu paranteză acoladă - {}
# O colecție de date care nu este indexată, sau ordonată, dar ordonează elementele când facem un type casting - int
# Set-urile nu permit valori duplicate
# Castul se face cu set()
items = [5, 2, 4, 5, 1, 8, 6, 9, 3, 2]
# items = {5, 2, 4, 5, 1, 8, 6, 9, 3, 2}
names = ["Felix", "Dumitru", "Radu", "Andrei", "Mihai", "Andrei"]
colegi = [("Andrei", 7), ("Ion", 10)]
employee = {
    "first_name": "Felix",
    "last_name": "Pericică",
    "age": 29,
    "years_old": 2.5,
    "bonus_applied": True
}
employees = {
    1: {
        "first_name": "Felix",
        "last_name": "Pericică",
        "age": 29,
        "years_old": 2.5,
        "bonus_applied": True
    },
    2: {
        "first_name": "Ion",
        "last_name": "Popescu",
        "age": 35,
        "years_old": 1.5,
        "bonus_applied": False
    }
}
print(f"Vârsta lui Ion Popescu este: {employees[2]['age']}")
# print(names)
# print(items)
# items = set(items)
# print(items)
# print(items[1]) # va genera o eroare

def process_list(items: list) -> list:
    return list(set(items))

# print(process_list(items))

# Declararea inițială pentru liste, tupluri, seturi
names = [] # names = list()
# print(type(names))
names = () # names = tuple()
# print(type(names))
names = set() # declararea names = {} nu îl va recunoaște drept set, ci dict
# print(type(names))

# 4. Dicționarul
# Stochează datele într-o pereche cheie-valoare
car = {
    "brand": "Volkswagen",
    "model": "Pasat CC",
    "year": 2017
}
# print(car)
# print(car["brand"]) # print(nume_variabila[cheie])
# print(car["model"]) # car.get("model")
# print(car["year"])
car["year"] = 2018
# print(car.items())
# items = list(car.items())
# print(items)
# print(len(car))
# print(car.values())
# print(items[1][1])
