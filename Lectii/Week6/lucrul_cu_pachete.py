# os = operating system
import os

current_directory = os.getcwd()
file = "test.txt"
path = os.path.join(current_directory, file)

# print(current_directory)
# print(path)
# for element in os.listdir(current_directory):
#     print(element)

# Pentru lucrul cu date
from datetime import datetime

now = datetime.now()
date_text = "2023-07-10"
date = datetime.strptime(date_text, "%Y-%m-%d")

# print(now)
# print()
# print(type(date_text))
# print(date)
# print(type(date))

# Pentru operațiuni matematice
import math

nr = 16
square_root = math.sqrt(nr)

# Scrierea cu majusculă se folosește pentru variabilele constante
PI = math.pi

print(square_root)
print(PI)
