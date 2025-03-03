import sqlite3
import os
import re
"""EXERCITIUL 1"""

"""
Write a SQL statement to create a table called continents, with the following columns:
continent_id
continent_name
continent_code – 2 letters code, use this link

"""

conn = sqlite3.connect("geografie.db")
cursor = conn.cursor()

# """ V1 """
# cursor.execute(
#     """
#     CREATE TABLE Continents(
#         continent_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         continent_name TEXT NOT NULL,
#         continent_code CHAR(2) NOT NULL
#     )
#     """
# )
#
# conn.commit()

""" EXERCITIUL 2 """

# current_directory = os.getcwd()
# file = 'info.txt'
# path = os.path.join(current_directory, file)
# continente = []
#
# with open(path, 'r') as continents_list:
#     for cont in continents_list:
#         delimiters_pattern = r',|\n'
#         continent = re.split(delimiters_pattern, cont)
#         cnt = []
#         for c in continent:
#             cnt.append(c)
#         continente.append(cnt)
#
#
# for i in range(len(continente)):
#     continente[i].remove(continente[i][2])
# print(continente)
#
# sql_query = f"INSERT INTO Continents(continent_name, continent_code) VALUES (?,?)"
# cursor.executemany(sql_query, continente)
# conn.commit()


# cursor.execute(
#     """
#     CREATE TABLE Countries(
#     country_code CHAR(2) PRIMARY KEY,
#     country_name TEXT NOT NULL,
#     continent_id INTEGER NOT NULL,
#     population INTEGER NOT NULL,
#     FOREIGN KEY (continent_id) REFERENCES Continents (continents_id)
#     );
#     """
# )
#
# conn.commit()

# sql_query = 'INSERT INTO Countries (country_code, country_name, continent_id, population) '\
#             'VALUES ("RO", "Romania", 6, 19000000)'
# cursor.execute(sql_query)
# conn.commit()

"""Exercitiul 7"""
# sql_query = 'SELECT * FROM Countries WHERE country_name LIKE "R%"'
# cursor.execute(sql_query)
# r = cursor.fetchall()
# print(r)

"""Exercitiul 8"""

# sql_query = 'INSERT INTO Countries (country_code, country_name, continent_id, population) '\
#             'VALUES ("NA", "Canada", 3, 40000000)'
# cursor.execute(sql_query)
# conn.commit()
#
# sql_query = 'INSERT INTO Countries (country_code, country_name, continent_id, population) '\
#             'VALUES ("US", "USA", 3, 330000000)'
# cursor.execute(sql_query)
# conn.commit()

# sql_query = 'SELECT * FROM Countries ORDER BY continent_id'
# cursor.execute(sql_query)
# r = cursor.fetchall()
# print(r)
#
# for i in range(10):
#     sql_query = f'SELECT continent_id, COUNT(country_name) FROM Countries WHERE continent_id = {i}'
#     cursor.execute(sql_query)
#     r = cursor.fetchone()
#     if r[0] is not None:
#         print(r)

"""Exercitiul 9"""

# for i in range(10):
#     sql_query = f'SELECT continent_id, SUM(population) FROM Countries WHERE continent_id = {i}'
#     cursor.execute(sql_query)
#     r = cursor.fetchone()
#     if r[0] is not None:
#         print(r)
