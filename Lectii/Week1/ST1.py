"""
Topice: variabile, cele mai uzuale tipuri de date, metode Python built-in
și diferite metode de lucru pentru șirurile de caractere.
"""

# Printeaza Hello World
# print('Hello World!')

# Variabila de tip str
# name = 'Felix C. Pericică'
# print(type(name))
# Variabila de tip int
# age = 29
# print(type(age))
# age = float(age)
# print(age, type(age))
# Variabila de tip float
# activity = 1.1
# Variabila de tip boolean
# is_married = False # snake case
# isMarried = False # camel case
# print(is_married)

def get_details(name: str, age: int, is_married: bool) -> str:
    """
    Retrieves info about a person.

    :param name: Name (str)
    :param age: Age (int)
    :param is_married: True or False (bool)
    :return: A full string with details.
    """
    details = f"Full Name: {name}, age {age}, and is married: {is_married}."
    # or return f"Full Name: {name}, age {age}, and is married: {is_married}."

    return details


details = get_details('Felix C. Pericică', 29, False)

# print(details)

# data = input("Enter something: ")
# print(int(data * 2))

# Diferite metode care se pot aplica șirurilor de caractere
name = 'felix'
print(name)
print(name.upper())
print(name.capitalize())
