import datetime
"""Exercitul 1"""

# def suma(a: int, b: int):
#     return a + b
#
# print(suma(1, 2))

"""Exercitiul 2"""


# def paritate(a: int):
#     if a % 2 == 0:  # 11
#         return True
#     return False
#
# # f(x) = x * x + 1
#
#
# print(paritate(11))

"""Exercitiul 3"""

# def nr_litere(nume: str, prenume: str, nume_mij:str):
#     return len(nume) + len(prenume) + len(nume_mij)
#
# print(nr_litere("Alexa", "Catalin", "Flavius"))

"""Exercitiul 4"""


# def aria(l: int, L: int):
#     return l * L
#
#
# print(aria(10, 20))

"""Exercitiul 5"""

#import math

# def aria_cercului(r: float): # 2.5
#     aria = math.pi * r * r
#     return aria
#
#
# def aria_cercului(r: float): # 2.5
#     aria = 3.14 * r * r
#     return aria
#
#
# print(aria_cercului(2.5))

"""Exercitiul 6"""

# string = input()
# caracter = input()
#
#
# def find_caracter(caracter: str, string: str):
#     if string.find(caracter) > 0:
#         return True
#     else:
#         return False
#
#
# print(find_caracter(caracter, string))

"""Exercitiul 7"""

# string = input()
#
# def c_upper(string: str):
#     cnt_upper = 0
#     for caracter in string:
#         if caracter.isupper():
#             cnt_upper += 1
#     return cnt_upper
#
# def c_lower(string: str):
#     cnt_lower = 0
#     for caracter in string:
#         if caracter.islower():
#             cnt_lower += 1
#     return cnt_lower
#
# print(c_upper(string))
# print(c_lower(string))

"""Exercitiul 8"""

# def numere(*numere):
#     numere_poz = []
#     for numar in numere:
#         if numar > 0:
#             numere_poz.append(numar)
#     return numere_poz
#
# print(numere(1, 2, 3, 4, 5, 6, 7, 8, 9, -1))

"""Exercitiul 9"""

# def numere(a: int, b: int):
#     if a > b:
#         print(f"Numarul {a} este mai mare decat {b}")
#     elif a < b:
#         print(f"Numarul {b} este mai mare decat {a}")
#     else:
#         print("Numerele sunt egale")
#
# numere(10, 20)


"""Exercitiul 10"""

# def exe_10(a: int, lista: list):
#     ok = False
#     for numar in lista:
#         if a == numar:
#             ok = True
#
#     if not ok:
#         print("Am adaugat numărul nou în set")
#         return ok
#     elif ok:
#         print("Nu am adaugat numărul în set. Acesta există deja")
#         return ok
#
# list = [10, 30, 40]
# print(exe_10(20, list))

"""Exercitiul 11"""


# def zile_luna(luna: int):
#     luna_zile = {
#         1: 31,
#         2: 28,
#         3: 31,
#         4: 30,
#         5: 31,
#         6: 30,
#         7: 31,
#         8: 31,
#         9: 30,
#         10: 31,
#         11: 30,
#         12: 31,
#     }
#         key   value
#     for luni, zile in luna_zile.items():
#         if luna == luni:
#             return zile
#
# print(zile_luna(3))

# def zile_luna(luna: str):
#     luna_zile = {
#         "Ianuarie": 31,
#         "Februarie": 28,
#         "Martie": 31,
#         "Aprilie": 30,
#         "Mai": 31,
#         "Iunie": 30,
#         "Iulie": 31,
#         "August": 31,
#         "Septembrie": 30,
#         "Octombrie": 31,
#         "Noiembrie": 30,
#         "Decembrie": 31,
#     }
#
#     for luni, zile in luna_zile.items():
#         if luna == luni:
#             return zile
#
# print(zile_luna("Iunie"))

"""Exercitiul 12"""

# def calculator(a: int, b: int):
#     suma = a + b
#     dif = abs(a - b)
#     inmultire = a * b
#     impartire = a / b
#
#     return suma, dif, inmultire, impartire
#
# a, b, c, d = calculator(10, 2)
#
# print("Suma: ", a)
# print("Diferenta: ", b)
# print("Inmultirea: ", c)
# print("Impartirea: ", d)

"""Exercitiul 13"""

# def zero_list_maker(n):
#     lista = [0] * n
#     return lista
#
# def dict_numere(lista: list):
#     lista_frecv = zero_list_maker(10)
#     for element in lista:
#         lista_frecv[element] += 1
#     frecvente = {
#         0: lista_frecv[0],
#         1: lista_frecv[1],
#         2: lista_frecv[2],
#         3: lista_frecv[3],
#         4: lista_frecv[4],
#         5: lista_frecv[5],
#         6: lista_frecv[6],
#         7: lista_frecv[7],
#         8: lista_frecv[8],
#         9: lista_frecv[9],
#     }
#
#     return frecvente
#
# lista = [1, 3, 1, 5, 9, 7, 7, 5, 5]
# print(dict_numere(lista))

"""Varianta 2"""

# def dict_numere(lista: list):
#     dictionar = {}
#     cnt = 0
#
#     for i in range(0, 10):
#         cnt = 0
#         for j in lista:
#             if j == i:
#                 cnt += 1
#         dictionar[i] = cnt
#     return dictionar
#
#
# dictionar = dict_numere(lista)
# print(dictionar)

"""Exercitiul 14"""

# def maxim_3(a, b, c):
#     return max(a, b, c)
#
# print(maxim_3(10, 20, 30))

"""Exercitiul 15"""


# def suma(n: int):
#     suma_nr = 0
#     for i in range(n + 1):
#         suma_nr += i
#
#     return suma_nr
#
# print(suma(10))

"""Exercitiul 16"""

list1 = [1, 1, 2, 3]
list2 = [2, 2, 3, 4]

"""Varianta 1"""

# def numere_dublate(list1: list, list2: list):
#     lista = []
#     for element in list1:
#         for element1 in list2:
#             if element == element1:
#                lista.append(element)
#     return set(lista)
#
# print(numere_dublate(list1, list2))

"""Varianta 2"""
# list1 = set(list1)
# list2 = set(list2)
#
# list3 = list1.intersection(list2)
#
# print(list3)

"""Exercitiul 17"""

"""Varinta 2"""
# pret = 100
#
# def reducere(redus: int):
#     if redus > 100:
#         print("Reducerea nu se poate aplica")
#     elif redus < 0:
#         print("Nu exista reducere")
#
# reducere(110)


"""Varianta 1"""
# pret = 100
#
# redus = int(input())
#
# def reducere(redus: int):
#     suma = 0
#
#     try:
#         suma = pret - pret * redus / 100
#         if suma < 0 or suma > pret:
#             raise Exception
#         print(f"Sunt reduceri la suma {suma}")
#
#     except Exception:
#         print("Nu este reducere")
#     finally:
#         print("Halal reduceri")
#
# print(reducere(redus))

"""Exercitiul 18"""

# def ora_zi():
#     x = datetime.datetime.now()
#     print(x)
#
# ora_zi()

"""Exercitiul 19"""

# from datetime import date
# d0 = date.today()  # data zilei de azi
# d1 = date(2023, 10, 10)
#
# delta = d1 - d0
# print(delta.days)





























"""Exercitiul 11"""


# def zile_luna(luna: int):
#     luna_zile = {
#         1: 31,
#         2: 28,
#         3: 31,
#         4: 30,
#         5: 31,
#         6: 30,
#         7: 31,
#         8: 31,
#         9: 30,
#         10: 31,
#         11: 30,
#         12: 31,
#     }
#         # key   value
#     for luni, zile in luna_zile.items():
#         if luna == luni:
#             return zile
#
# print(zile_luna(3))

# def zile_luna(luna: str):
#     luna_zile = {
#         "Ianuarie": 31,
#         "Februarie": 28,
#         "Martie": 31,
#         "Aprilie": 30,
#         "Mai": 31,
#         "Iunie": 30,
#         "Iulie": 31,
#         "August": 31,
#         "Septembrie": 30,
#         "Octombrie": 31,
#         "Noiembrie": 30,
#         "Decembrie": 31,
#     }
#
#     for luni, zile in luna_zile.items():
#         if luna == luni:
#             return zile
#
# print(zile_luna("Iunie"))



"""Exercitiul 12"""


# def calculator(x, y):
#     return x + y, x - y, x * y, x / y
#
#
# a, b, c, d = calculator(10, 2)
# print(f'Suma: {a} ')
# print(f'Diferenta: {b} ')
# print(f'Inmultirea: {c} ')
# print(f'Impartirea: {d} ')


"""Exercitiul 15"""


# def suma(n: int):
#     suma_nr = 0
#     for i in range(n + 1):
#         suma_nr += i
#
#     return suma_nr
#
# print(suma(10))


"""Exercitiul 16"""

# lista1 = [1, 1, 2, 3, -2, -8, -10]
# lista2 = [2, 2, 3, 4, 4, 5, 6, 7, 8, 9, -1, -2, -5, -10]
#
#
# def primeste_liste(list1, list2):
#     return set(list1).intersection(list2)
#
#
# listanoua = primeste_liste(list1, list2)
# print(listanoua)


"""Exercitiul 19"""

# from datetime import date
# d0 = date.today()  # data zilei de azi
# d1 = date(2023, 10, 10)
#
# delta = d1 - d0
# print(delta.days)