# #o variabila este un obiect folosit pentru a putea exprima o valoare in mod reutilizabil
#
# animal = 'Leu'
# age = 17
# bani = 1000000.10
# am_permis = False
#
# print(type(animal), type(age), type(bani), type(am_permis))
#
# bani = round(bani)
# print(bani)
#
# print(animal + " este un animal")
# print(str(age) + " este un numar")
# print(str(bani) + " este float")
# print(str(am_permis) + " am permis")



# nume, prenume = input().split()
# numar_caractere = len(nume) + len(prenume)
#
# print("Numele complet are " + str(len(nume) + len(prenume)) + " caractere")



# nume = input("Introdu numele tau: ")
# prenume = input("Introdu prenumele tau: ")
# prenume2 = input()
#
# print(f'Numele complet este {nume}, iar prenumele este {prenume} {prenume2} si numele are {len(nume) + len(prenume)} caractere')


"""
Cerinta 7
"""
#import numbers

# lungime = input()
# latime = input()
#
# print("Aria dreptungiului este " + str(int(lungime) * int(latime)))

"""
Cerinta 8
"""
# prop = "Coral is either the stupidest animal or the smartest rock"
# cuvinte = prop.split() [Coral, is, either...
# cnt = 0
#
# for cuvant in cuvinte:
#      if cuvant == "the":
#         cnt += 1
#
# #print(cnt)
#
# ok = True
#
# for cuvant in cuvinte:
#     assert cuvant.isalpha()
#     ok = False
#
# print(ok)

"""
Cerinta 11
"""

# impar_string = input()
# litera_mijloc = len(impar_string)
# print(impar_string[int(litera_mijloc / 2) : int(litera_mijloc / 2) + 1])

"""
Cerinta 12
"""

#propozitie = input(); cuvant1 = propozitie.split()[0]; cuvant2 = propozitie.split()[1];print(cuvant1 + ' ' + cuvant2)

"""
Cerinta 13
"""

# cuvant = input()
# caracter = cuvant[0:1] # a
# cnt = -1
# lungime = len(cuvant)
#
# for caracter1 in cuvant:
#     cnt += 1
#     if cnt == 0 or cnt == lungime - 1:
#         print(caracter1, end = "")
#     elif caracter1 == caracter:
#         print(caracter1.capitalize(), end = "")
#     else:
#         print(caracter1, end = "")
#
# #     #print(' ' + str(cnt) + ' ')
# # alAbAlA portocAla
""" 
Cerinta 14
"""

# user = input()
# parola = input()
#
# print("Parola pentru user-ul " + user + " este", end= " ")
#
# # for i in range(len(parola)):
# #     print("*", end = " ")
#
# print( '*' * len(parola), end = "")
#
# print(" si are " + str(len(parola)) + " caractere")

"""
Cerinta 1
"""

#un if else functioneaza in felul urmator: daca, cinditia din if se indseplineste aceasta scrie ceea ce i-am dat noi sa scrie altfel va scrie
#cealalta expresie

"""
Cerinta 2
"""

#x = 10000
#y = 10
# if type(x) == int:
#     print("DA")
# else:
#     print("NU")

"""
Cerinta 3
"""

# if x < 0:
#     print("Negativ")
# elif x == 0
#     print("Netru")
# elif x > 0:
#     print("Pozitiv")


"""
Cerinta 4
"""

# if x >= -2 and x <= 13:
#     print("Este inclus")
# else:
#     print("Nu este inclus")

"""
Cerinta 5
"""
# if x - y < 5:
#     print("NU")
# else:
#     print("DA")

"""
Cerinta 6
"""
# if not x >= 5  and x <= 27:
#     print("NU")
# else:
#     print("DA")


"""
Cerinta 7
"""

# if x == y:
#     print("Egale")
# elif x < y:
#     print(str(y))
# else:
#     print(str(x))

"""
Cerinta 8
"""

# a = 10
# b = 10
# c = 10
#
# if a == b and a != c:
#     print("Isoscel")
# elif a == b and b == c:
#     print("Echilateral")
# elif a != b and b != c and c != a:
#     print ("Oarecare")

"""
Cerinta 9
"""

# vocala = input()
#
# if vocala == 'a':
#     print("E vocala")
# if vocala == 'e':
#     print("E vocala")
# if vocala == 'i':
#     print("E vocala")
# if vocala == 'o':
#     print("E vocala")
# if vocala == 'u':
#     print("E vocala")

"""
Cerinta 10
"""

# nota = input()

# if int(nota) == 9:
#     print("A")
# if int(nota) == 8:
#     print("B")
# if int(nota) == 7:
#     print("C")
# if int(nota) == 6:
#     print("D")
# if int(nota) == 5:
#     print("E")
# if int(nota) <= 4:
#     print("F")

"""
Cerinta 11
"""

# numar = input()
#
# verifica_int = int(numar) / 1000
#
# if int(verifica_int) >= 1:
#     print("Are minim patru cifre")
# else:
#     print("Nu are patru cifre")


"""
Cerinta 12
"""

# numar = input()
#
# nr_cifre = int(numar) / 100000
#
# if int(nr_cifre <= 9) and int(nr_cifre >= 1):
#     print("Are fix 6 cifre")
# else:
#     print("Nu are 6 cifre")


"""
Cerinta 13
"""

# numar = input()
#
# if int(numar) % 2 == 0:
#     print("Este numar par")
# else:
#     print("Este numar impar")

"""
Cerinta 14
"""

# x, y, z = input().split()
#
# maximul = max(int(x), int(y), int(z))
#
# print(maximul)

"""
Cerinta 15
"""

# x, y, z = input().split()
#
# if x + y + z == 180:
#     print("Este valid")
# else:
#     print("Nu este valid")

"""
Cerinta 16
"""

# x = input()
# propozitie = "Coral is either the stupidest animal or the smartest rock"
#
# for i in range(len(propozitie) - int(x)):
#     print(propozitie[i], end = "")

"""Cerinta 17"""

# propozitie = "Coral is either the stupidest animal or the smartest rock"
# primul_cuvant = propozitie[0:5]
# lungime = len(propozitie)
# ultimul_cuvant = propozitie[lungime - 5 : lungime]
#
# cuvant = primul_cuvant + ultimul_cuvant
# print(cuvant)

"""Cerinta 18"""

# propozitie = "Coral is either the stupidest animal or the smartest rock"
# x = propozitie.find("rock")
#
# print(x, end = " ")
#
# for i in  range(x):
#    print(propozitie[i], end ="")


"""Cerinta 19"""

# import random
# random_number = random.randint(1, 6)
#
# user_number = input()
#
# if int(user_number) > random_number:
#     print("Ai pierdut.Ai ales un numar mai mare!" + "Ai ales " + user_number + " dar a fost " + str(random_number))
# if int(user_number) < random_number:
#     print("Ai pierdut.Ai ales un numar mai mic"+ "Ai ales " + user_number + " dar a fost " + str(random_number))
# if int(user_number) == random_number:
#     print("Ai ghicit!Felicitari!"+ "Ai ales " + user_number + " si a fost " + str(random_number))

"""Cerinta 20"""

# string = input()
# string_length = len(string)
# prima_litera = string[0].capitalize()
# ultima_litera = string[string_length - 1].capitalize()
#
# assert str(prima_litera) == str(ultima_litera), "Sunt litere diferite"
#
# assert str(prima_litera) != str(ultima_litera), "Sunt aceleasi diferite"

"""Cerinta 21"""

# numar = "0123456789"
#
# for i in range(len(numar)):
#     if int(numar[i]) % 2 == 0:
#         print(numar[i], end = " ")
#
# print('\n')
#
# for i in range(len(numar)):
#     if int(numar[i]) % 2 == 1:
#
#
# print(numar[i], end = " ")