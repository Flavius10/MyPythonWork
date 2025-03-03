"""
Topice:
    1. Tipurile principale de operatori (de atribuire, aritmetici, de comparare, logici);
    2. Fluxul de control logic (if-elif-else);
    3. String Slicing.
"""
# Operatorul „=” face o atribuire de valoare unei variabile (asignare)
name = 'Felix C. Pericică'

# Operatori de atribuire: =, +=, -+, *=, /=
age = 29
print("Variabila initiala:", age)
age += 1 # age = age + 1
print("Variabila incrementata:", age)
age -= 1 # age = age - 1
print("Variabila decrementata:", age)
age *= 2 # age = age * 2
print("Variabila inmultita:", age)
age /= 2 # age = age / 2
print("Variabila impartita:", age)

# Operatorii aritmetici: +, -, *, /, %, **, //, -
# + este operator matematic sau concatenator
numar_1 = 10
numar_2 = 20
adunare = numar_1 + numar_2 # variabilele trebuie să fie int
# adunare = "numar_1" + "str"
print("Variabila dupa aplicarea procesului de adunare:", adunare)
scadere = numar_2 - numar_1
print("Variabila dupa aplicarea procesului de scadere:", scadere)
inmultire = numar_1 * numar_2
print("Variabila dupa aplicarea procesului de inmultire:", inmultire)
impartire = numar_2 / numar_1
print("Variabila dupa aplicarea procesului de impartire:", impartire)
modulo = numar_2 % numar_1
print("Variabila dupa aplicarea operatorului modulo:", modulo)
exponent = numar_2 ** 2
print("Variabila dupa aplicarea operatorului exponential:", exponent)
floor_division = 7 // 2 # 3.5
print("Variabila dupa aplicarea operatorului 'floor division':", floor_division)

# Operatori de comparație: ==, !=, <, <=, >, >=
print(numar_1 == numar_2) # False
print(numar_1 != numar_2) # True
print(numar_1 < numar_2) # True
print(numar_1 <= numar_2) # True
print(numar_1 > numar_2) # False
print(numar_1 >= numar_2) # False

# Operatori logici: and, or, not
is_married = True
has_kids = None
has_license = False # '' sau None sau 0
age = 19 # True
print(is_married and has_kids) # ambele condiții trebuie îndeplinite
print(is_married or has_kids) # doar o condiție trebuie îndeplinită
print(not is_married) # opusul condiției de verificat
print(has_license or age)

# Fluxul de control logic: if-elif-else
# if condition:
#   something_happens
# elif another_condition:
#   another_thing_happens
# else:
#   default
def check_fizz(number: int) -> str:
    """
    FizzBuzz game.

    :param number: number (int)
    :return: Fizz if number divides with 3, Buzz if it divides with 5, FizzBuzz if it divides with 15.
    """
    if number % 15 == 0:
        print("FizzBuzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0:
        print("Fizz")
    else:
        print("Else")


check_fizz(15)


def check_car(make: str, km: float, years_old: int, has_license: bool):
    if has_license:
        string = "da"
    else:
        string = "nu"

    return f"Mașină: {make}, km în bord: {km}, ani vechime: {years_old}, {string}, are permis."


print(check_car("Volvo", 85000.500, 10, False))
print(check_car("Toyota", 95000.500, 15, True))

# Python Slicing
# string[start:stop:step]
# Working on name = "Felix C. Pericică"
first_name = name[:5]
last_name = name[9:]
print(first_name)
print(last_name)
print(first_name[-1]) # index negativ = ultimul caracter
print(first_name[::-1]) # șirul de caractere inversat
