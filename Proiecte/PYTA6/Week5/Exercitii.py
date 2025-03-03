import random
import time
from datetime import date
from abc import ABC, abstractmethod

"""Exercitiul 1"""


# class PresedinteRomania(object):
#
#     __instance = None
#
#     def __str__(self):
#         return "Eu sunt presedintele Romaniei"
#
#     def __new__(cls, *args):
#         if cls.__instance is None:
#             cls.__instance = object.__new__(cls)
#         return cls.__instance
#
#     def say_hello(self):
#         return f"Salut {self}"
#
#
# if __name__ == "__main__":
#     a = PresedinteRomania()
#     b = PresedinteRomania()
#     print(f"ID(a): {id(a)}")
#     print(f"ID(b): {id(b)}")
#     print(a is b)
#     print(a.say_hello())


"""Exercitiul 2"""


# class Language(ABC):
#
#     @abstractmethod
#     def localize(self, cuvant: str):
#         pass
#
#
# class English(Language):
#
#     translations = {"masina": "car"}
#
#     def localize(self, cuvant: str):
#         if cuvant in self.translations:
#             return self.translations[cuvant]
#         else:
#            return "Ba ,nu stiu sa iti traduc"
#
#
# class Spanish(Language):
#
#     translations = {"masina": "coche"}
#
#     def localize(self, cuvant: str):
#         if cuvant in self.translations:
#             return self.translations[cuvant]
#         else:
#             return "Ba ,nu stiu sa iti traduc"
#
#
# class French(Language):
#
#     translations = {"masina": "voiture"}
#
#     def localize(self, cuvant: str):
#         if cuvant in self.translations:
#             return self.translations[cuvant]
#         else:
#             return "Ba ,nu stiu sa iti traduc"
#
#
# class TranslatorFactory:
#
#     language = {"en": English, "es": Spanish, "fr": French}
#
#     @classmethod
#     def get_translator(cls, limba: str):
#         if limba in cls.language:
#             return cls.language[limba]()
#         raise KeyError(f"Traducatorul nu a fost gasit cu datele din parametru {limba}")
#
#
# if __name__ == "__main__":
#     factory = TranslatorFactory()
#
#     english_trans = factory.get_translator('en')
#     spanish_trans = factory.get_translator('es')
#     french_trans = factory.get_translator('fr')
#
#     print(f'In engleza zicem {english_trans.localize("masina")}')
#     print(f'In spaniola zicem {spanish_trans.localize("masina")}')
#     print(f'In franceza zicem {french_trans.localize("masina")}')
#

"""Exercitiul 3"""


# def lotto(n):
#     while n > 1:
#         random1 = random.randint(1, 49)
#         yield random1
#         n -= 1
#     if n == 1:
#         yield "4 7 9 6 2 3 1"
#
#
# if __name__ == "__main__":
#     for loto in lotto(7):
#         print(loto)


"""Exercitiul 4"""


# def opn1():
#     open_file = open('hello', 'r')
#     try:
#         read_file = open_file.read()
#         print(read_file)
#     finally:
#         open_file.close()
#
#
# def opn2():
#     with open('hello', 'r') as file:
#         read_line = file.read()
#         print(read_line)
#
# if __name__ == "__main__":
#     opn1()
#     opn2()


"""Exercitiul 5"""


# def timeit(function):
#     def timp(*args, **kwargs):
#         result = function(*args, **kwargs)
#         print(f"Timpul de executie este: {result}")
#
#     return timp
#
#
# @timeit
# def timpul():
#     start = time.time()
#     print("Hello")
#     end = time.time()
#     return start - end

#
# def timpul2():
#     start = time.time()
#     print("Hello")
#     end = time.time()
#     return start - end
#
#
# if __name__ == "__main__":
#     timpul()
#     print("-" * 40)
#     print(timpul2())


"""Exercitiul 6"""


# def require_login(function):
#     def decorator(*args, **kwargs):
#         result = function(*args, **kwargs)
#         print(f"Datele userului sunt: {result}")
#
#     return decorator
#
#
# class User:
#
#     __logat = None
#
#     def __init__(self, nume: str, email: str, parola: str, data_nasterii: str):
#         self.nume = nume
#         self.email = email
#         self.parola = parola
#         self.data_nasterii = data_nasterii
#
#     def login(self, email: str, parola: str):
#         if email == "flaviusa1010@gmail.com" and parola == "parola" and User.__logat is None:
#             User.__logat = User(self.nume, self.email, self.parola, self.data_nasterii)
#
#     @require_login
#     def get_info(self):
#         if User.__logat is not None:
#             return f"{self.nume}, {self.email}, {self.parola}, {self.data_nasterii}"
#         else:
#             return f"N/A"
#
#     def logout(self):
#         if User.__logat is not None:
#             User.__logat = None
#
#
# user = User("Flavius", "email", "parola", "10.10.2005")
# user.get_info()
# user.login("flaviusa1010@gmail.com", "parola")
# user.get_info()
# user.logout()
# user.get_info()
# user.login("flaviusa1010@gmail.com", "parola")
# user.get_info()
#
