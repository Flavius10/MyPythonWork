import pandas as pd
import string,os
import json
import csv
from tabulate import tabulate


"""Exercitiul 1"""
# current_directory = os.getcwd()
# file_name = 'hello.txt'
# path = os.path.join(current_directory, file_name)

# with open("hello.txt", 'r', encoding='utf-8') as open_file:
#     read_file = open_file.read()
#     print(read_file)
#
# with open(path, 'r', encoding='utf-8') as open_file:
#     read_file = open_file.read()
#     print(read_file)

"""Exercitiul 2"""

# file_append = ['Go', 'Kotlin', 'Swift']

# with open(path, 'a', encoding='utf-8') as file_app:
#     for i in range(len(file_append)):
#         file_app.write(file_append[i] + '\n')

# with open(path, 'r', encoding='utf-8') as open_file:
#     read_file = open_file.read()
#     print(read_file)

"""Exercitiul 3"""

# with open(path, 'r', encoding='utf-8') as exer_3:
#     linii = exer_3.readlines()
#     for i in range(len(linii)):
#         if i % 2 == 1:
#             print(linii[i])

"""Exercitiul 4"""


# ordinals = {'1st': 'A', '2nd':'B', '3rd':'C', '4th':'D', '5th':'E', '6th':'F', '7th':'G', '8th':'H', '9th':'I', '10th':'J'
#  ,'11th': 'K', '12th': 'L', '13th':'M', '14th':'N', '15th':'O', '16th':'P', '17th':'Q', '18th':'R', '19th':'S'
#  ,'20th':'T', '21st':'U', '22nd':'V', '23rd':'W', '24th':'X', '25th':'Y', '26th':'Z'}
#
#
# for poz, letter in ordinals.items():
#     with open(letter.upper() + ".txt", 'w') as f:
#         f.writelines(f"My name is letter {letter}" + '\n')
#         f.writelines(f"I am the {poz} letter of the alphabet.")
#


"""Exercitiul 5"""

"""Metoda 1"""

# with open("students.csv", 'r', encoding='utf-8') as file_read:
#     csv_readfile = csv.reader(file_read)
#     first_row = True
#     for row in csv_readfile:
#         if first_row:
#             for i in range(len(row)):
#                 print(row[i], end=" ")
#             print("\n")
#             print("-" * 25)
#             first_row = False
#             print("\n")
#         else:
#             for i in range(len(row)):
#                 print(row[i], end=" ")
#             print("\n")
#
# """Metoda 2"""
#
# read_data = pd.read_csv("students.csv")
# print(read_data)

"""Exercitiul 6"""

# data = []
# data_first_line = []
#
# with open("students.csv", 'r', encoding='utf-8') as file:
#     csv_file = csv.reader(file)
#     first_line = True
#     for row in csv_file:
#         if first_line:
#             data_first_line.extend(row)
#             first_line = False
#         else:
#             data.append(row)
#
# data1 = {}
# data_dictionar = {}
# dictionar = []
#
# for i in range(len(data)):
#     data1 = {}
#     for j in range(len(data_first_line)):
#         data1[data_first_line[j]] = data[i][j]
#     data_dictionar[i] = data1
#
# print(data_dictionar)
#
# with open("students.json", 'a') as file:
#     json.dump(data_dictionar, file)

