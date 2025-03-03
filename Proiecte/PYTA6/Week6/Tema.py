from abc import ABC, abstractmethod
#
# """
# A.    Pentru Singelton (Un CEO intr-o intreprindere)
# A se crea mai multe metode pentru a crea continut
# B.    Cum putem implementa “Factory” in cazul unei cafele si sa returneze reteta, dupa selectarea produsului dorit
# Sortimente: Capucino, Latte Machiato si Americano
#
# """
#
#
"""A"""
#
#
# class CEO(object):
#     __instance = None
#
#     def __str__(self):
#         return "Eu sunt Flavius, CEO-ul acestei companii"
#
#     def __new__(cls, *args):
#         if cls.__instance is None:
#             cls.__instance = object.__new__(cls)
#         return cls.__instance
#
#     def prezentare(self):
#         return f"Salut {self}"
#
#     def prezentarea_echipei(self):
#         return "Echipa noastra este...."
#
#
# ceo = CEO()
# print(ceo)
# print(ceo.prezentare())
# print(ceo.prezentarea_echipei())
#
#
"""B"""
#
#
# class Recipe(ABC):
#
#     @abstractmethod
#     def recipe(self):
#         pass
#
#
# class Cappuccino(Recipe):
#     recipes = {"lapte": "50ml", "cafea": "40ml"}
#
#     def recipe(self):
#         print(f"Reteta pentru cappucino este:")
#         for elem, i in self.recipes.items():
#             print(elem + ":" + i)
#
#
# class LatteMachiato(Recipe):
#     recipes = {"lapte": "100ml", "cafea": "40ml"}
#
#     def recipe(self):
#         print(f"Reteta pentru latte machiato este:")
#         for elem, i in self.recipes.items():
#             print(elem + ":" + i)
#
#
# class Americano(Recipe):
#     recipes = {"lapte": "100ml", "cafea": "2000ml"}
#
#     def recipe(self):
#         print(f"Reteta pentru americano este:")
#         for elem, i in self.recipes.items():
#             print(elem + ":" + i)
#
#
# class CoffeFactory:
#     types = {"Cappuccino": Cappuccino, "LatteMachiato": LatteMachiato, "Americano": Americano}
#
#     @classmethod
#     def order_coffee(cls, coffee: str):
#         if coffee in cls.types:
#             return cls.types[coffee]()
#         raise KeyError(f"Nu avem cafea {coffee}, dar daca doriti ne puteti da reteta")
#
#
# if __name__ == "__main__":
#     cafea = CoffeFactory()
#
#     c = cafea.order_coffee("Cappuccino")
#     la = cafea.order_coffee("LatteMachiato")
#     a = cafea.order_coffee("Americano")
#
#     c.recipe()
#     print('\n')
#     a.recipe()
#     print('\n')
#     la.recipe()
