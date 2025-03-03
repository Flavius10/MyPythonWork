"""Exercitiul 1"""

# note_muzicale = ['DO', 'RE', 'MI', 'FA', 'SOL', 'LA', 'SI', 'DO']

# print(note_muzicale)
#
# note_muzicale = note_muzicale[::-1]
#
# print(note_muzicale)
#
# def inverseaza_note(note_muzicale : list)->list:
#     note_muzicale = note_muzicale[::-1]
#     return note_muzicale
#
# print(inverseaza_note(note_muzicale))


"""Exercitiul 2"""

# cnt = 0
#
# for note in note_muzicale:
#     if note == 'DO':
#         cnt += 1
#
# print(cnt)

"""Exercitiul 3"""

# lista1 = [3, 1, 0, 2]
# lista2 = [6, 5, 4]
#
# lista3 = lista1 + lista2
# print(lista3)
#
# lista3 = [*lista1, *lista2]
# print(lista3)

"""Exercitiul 4"""

# lista3 = set(lista3)
# print(lista3)

# def remove_from_list(lista : list)->list:
#     lista.remove(0)
#     return lista
#
# print(remove_from_list(lista3))

"""Exercitiul 5"""

# if len(lista3) != 0:
#     print("Lista nu este goală")
# else:
#     print("Lista este goală")

"""Exercitiul 6"""
# while lista3:
#     lista3.pop()

# print(lista3)

"""Exercitiul 7"""
# if len(lista3) != 0:
#     print("Lista nu este goală")
# else:
#     print("Lista este goală")

"""Exercitiul 8"""

# dict1 = {
#     'Ana': 8,
#     'Gigel': 10,
#     'Dorel': 5
# }
#
# for keys, elem in dict1.items():
#     print(keys)

"""Exercitiul 9"""

# dict1 = {
#     'Ana': 8,
#     'Gigel': 10,
#     'Dorel': 5
# }
#
# for keys, elem in dict1.items():
#     print(f'{keys} a luat nota {elem}')

"""Exercitiul 10"""

# dict1 = {
#     'Ana': 8,
#     'Gigel': 10,
#     'Dorel': 5
# }
#
# dict1['Dorel'] = 6
#
# print(dict1['Dorel'])


"""Exercitiul 11"""
#
# dict1 = {
#     'Ana': 8,
#     'Gigel': 10,
#     'Dorel': 5
# }
#
# dict1.pop('Gigel')
#
# print(dict1)
#
# dict1['Ionică'] = 9
#
# print(dict1)

"""Exercitiul 12"""

# jucatori_teren = ['Flavius', 'Catalin', 'Luca', 'Mihai', 'Alin']
# jucatori_banca = ['Mage', 'Radu', 'Alex']
# schimbari_efectuate = 0
# schimbari_max = 3
#
# jucatori = jucatori_banca + jucatori_teren

# def e_in_teren(jucator:str)->bool:
#     for juc in jucatori_teren:
#         if jucator == juc:
#             return True
#
# jucator_scos = None
# jucator_intrat = None

# for jucator in jucatori:
#     if jucator in jucatori_teren and schimbari_efectuate < 3:
#         jucatori_teren.remove(jucator)
#         jucatori_teren.append(jucatori_banca[schimbari_efectuate])
#         schimbari_efectuate += 1
#         print(f"A intrat {jucatori_banca[schimbari_max - schimbari_efectuate]}, a ieșit {jucator}, mai ai {schimbari_max - schimbari_efectuate} schimbări")
#     if jucator in jucatori_banca and schimbari_efectuate < 3:
#         print(f"Nu se poate efectua schimbarea deoarece jucătorul {jucator} nu e în teren")
#         print(f"Mai ai {schimbari_max - schimbari_efectuate} schimbari")

# for juc in jucatori:
#     if e_in_teren(juc) and schimbari_efectuate < 3:
#         jucatori_teren.remove(juc)
#         jucator_scos = juc
#         schimbari_efectuate += 1
#         print(f'A intrat {jucator_intrat}, a ieșit {jucator_scos}, mai ai {schimbari_max - schimbari_efectuate} schimbări')
#     elif not e_in_teren(juc):
#         jucatori_teren.append(juc)
#         jucator_intrat = juc
#         print(f'Nu se poate efectua schimbarea deoarece jucătorul {juc} nu e în teren')
#         print(f'Mai ai {schimbari_max - schimbari_efectuate} schimbări')

"""Exercitiul 13"""

# zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
# weekend = {'sâmbăta', 'duminică'}

# zile_sapt.add('luni')
# #
# # print(zile_sapt)
#

"""Exercitiul 14"""
#
# z = zile_sapt.intersection(weekend)
#
# if len(z) != 0:
#     print("Este un subset")
# else:
#     print("Nu este un subset")

"""Exercitiul 15"""
#
# z = zile_sapt.symmetric_difference(weekend)
#
# print(z)

"""Exercitiul 16"""
#
# z = zile_sapt.intersection(weekend)
#
# print(z)

"""Exercitiul 1"""

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']

# x = 2
#
# for masina in range(len(masini)):
#     if masina == 2:
#         print(masini[masina])

# lungime = 1
# while lungime < len(masini):
#     if lungime == 2:
#         print(f"Masina mea preferata este e {masini[lungime]}")
#     lungime += 1

"""Exercitiul 2"""

# for masina in range(len(masini)):
#     if masina != 0 and masina != len(masini) - 1:
#         masini[masina] = masini[masina].upper()
# else:
#         print(masini)
#
# for masina in range(len(masini)):
#     if masina == 0 or masina == len(masini) - 1:
#         masini[masina] = masini[masina]
#     else:
#         masini[masina] = masini[masina].upper()
# print(masini)
#
# for i in range(1, len(masini) - 1):
#     masini[i] = masini[i].upper()
#
# print(masini)


"""Exercitiul 3"""

# for masina in masini:
#     if masina == 'Mercedes':
#         print('Am găsit mașina dorită de dvs')
#         break
#     else:
#         print(f"Am gasit masina {masina}.Mai cautam")

"""Exercitiul 4"""

# for masina in masini:
#     if masina == 'Trabant' or masina == "Lăstun":
#         continue
#     print(f"S-ar putea să vă placă mașina {masina}")


"""Exercitiul 5"""

# masini_vechi = []
#
# for i in range(len(masini)):
#     if masini[i] == 'Lăstun' or masini[i] == 'Trabant':
#         masini_vechi.append(masini[i])
#         masini[i] = 'Tesla'
#
# print(masini_vechi)
# print(masini)


"""Exercitiul 6"""

# pret_masini = {
#     'Dacia': 6800,
#     'Lăstun': 500,
#     'Opel': 1100,
#     'Audi': 19000,
#     'BMW': 23000
# }
#
# for masina, pret in pret_masini.items():
#    if pret <= 15000:
#        print(f"Pentru un buget de 15000 de euro va puteti achizitiona masina {masina} la pretul de {pret} euro")
#

"""Exercitiul 7"""

# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
#
# cnt = 0
#
# for i in range(len(numere)):
#     if numere[i] == 3:
#         cnt += 1
#
# print(cnt)

"""Exercitiul 8"""

# suma = 0
#
# for numar in numere:
#     suma += numar
#
# print(suma)

"""Exercitiul 9"""

# maxim = 0
#
# for numar in numere:
#     if numar > maxim:
#         maxim = numar
#
# print(maxim)

"""Exercitiul 10"""

# for i in range(len(numere)):
#     if numere[i] > 0:
#         numere[i] -= numere[i] * 2
#
# print(numere)


"""Exercitiul 11"""

# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere_pare = []
# numere_impare = []
# numere_pozitive = []
# numere_negative = []
#
# cnt_pare = 0
# cnt_impare = 0
# cnt_poz = 0
# cnt_neg = 0
#
# for i in range(len(alte_numere)):
#     if alte_numere[i] % 2 == 0:
#         cnt_pare += 1
#         numere_pare.insert(cnt_pare, alte_numere[i])
#     if alte_numere[i] % 2 == 1:
#         cnt_impare += 1
#         numere_impare.insert(cnt_impare, alte_numere[i])
#     if alte_numere[i] > 0:
#         cnt_poz += 1
#         numere_pozitive.insert(cnt_poz, alte_numere[i])
#     if alte_numere[i] < 0:
#         cnt_neg += 1
#         numere_negative.insert(cnt_neg, alte_numere[i])
#
# print(numere_pozitive, numere_negative, numere_impare, numere_pare)

"""Exercitiul 12"""

# i = 0
# j = i + 1
#
# for i in range(len(alte_numere)):
#     for j in range(len(alte_numere)):
#         if alte_numere[i] < alte_numere[j]:
#             aux = alte_numere[i]
#             alte_numere[i] = alte_numere[j]
#             alte_numere[j] = aux
#
# print(alte_numere)

"""exercitiul 13"""

# import random
#
# numar_sercret = random.randint(1, 30)
# numar_ghicit = None
#
# while numar_ghicit != numar_sercret:
#     numar_ghicit = int(input())
#     if numar_ghicit < numar_sercret:
#         print("Nr secret e mai mare")
#     elif numar_ghicit > numar_sercret:
#         print("Nr secret e mai mic")
#     elif numar_ghicit == numar_sercret:
#         print("Felicitări! Ai ghicit!")

"""Exercitiul 14"""
# x = int(input())
# i = 1
#
# for i in range(1, x + 1):
#     y = i
#     while y >= 2:
#         print(i, end = "")
#         y -= 1
#
#     print(i, end = '\n')

# for i in range(1, x + 1):
#     print(str(i) * i)

"""Exercitiul 15"""

# tastatura_telefon = [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9],
#   [0]
# ]
#
# for lista in tastatura_telefon:
#     for cifra in lista:
#         print(f"Cifra curenta este {cifra}")
