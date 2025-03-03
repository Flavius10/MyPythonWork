"""
Topic principal: Funcții și Excepții

O funcție este un bloc de cod care este scris o singură dată
și poate fi refolosit ulterior ori de câte ori avem nevoie.

def nume_functie(parametri: tipul_de_date) -> tipul_de_date_returnat:
  '''
  Docstring care include o scurtă descriere a funcției, parametrii pe care îi primește drept input
  cu tipul lor, ce returnează funcția.
  '''
  codul de executat...

Avem mai multe tipuri de parametri:
  1. Parametri poziționali: def add_two_numbers(a, b): pass
  2. Parametri opționali: def hay_hello(name=None): pass
  3. Parametri by default: def hay_hello(name="Name"): pass
  4. Număr variabil de parametri:
    4.1. Simpli: def add_numbers(*numbers): pass
    4.2. De tip cheie-valoare: def add_numbers(**numbers): pass

Try-Except-Else-Finally este o structură de cod care ne permite să tratăm gestionarea erorilor
într-un mod cât mai elegant.

try:
  cod_de_executat()
except Error as e:
  do_something_with_error(e)
else:
  cod_de_executat_cand_nu_apare_eroarea()
finally:
  acest_cod_se_executa_mereu()
"""
# Putem folosi 'pass' pentru a sări linia de cod
# def subtract_two_numbers():
#     pass

# Semnătura funcției
# Parametrii se declară în semnătura funcției
def add_two_numbers(a: int, b: int) -> int:
    """
    Adds two different numbers and returns the result.

    :param a: int
    :param b: int
    :return: int
    """
    sum = a + b
    print(sum)

# Apelăm funcția / function call
# Argumentele sunt valorile reale pe care le pasăm funcției în call
add_two_numbers(2, 4)

# Exemplu de funcție cu parametru opțional


def say_hello(name = None):
    if name:
        return f"Hello, {name}!"

    return "Hello!"

# print(say_hello())
# salut = say_hello("Felix")
# print(salut)

# Exemplu cu parametru by default
def hello_world(name = "World!"):
    return f"Hello {name}"


# print(hello_world())
# print(hello_world("Felix"))
# print("-"*20)

# Exemplu de funcție cu număr variabil de parametri (simpli)
def print_numbers(*numbers):
    for number in numbers:
        pass
        # print(number)

def add_numbers(*numbers):
    return sum(numbers)

print_numbers(3, 4, 5, 6, 7)
# print(add_numbers(2, 3, 4, 5))


# Exemplu de funcție cu parametri variabili de tip cheie-valoare
def print_employees(**employees):
    for key, value in employees.items():
        pass
        # print(f"{key}: {value}")


print_employees(name="Felix", function="Python Developer", nume="Ioana", functie="Tester")

# Exemplu de funcție cu return multiplu
def is_natural(a: int) -> str:
    if a >= 0:
        return "Numărul este natural."
    else:
        return "Numărul nu este natural."

# print(is_natural(5))
# print(is_natural(-2))

items = [1, 2, 3, 4]
# print(items[0]) # va accesa elementul de la indexul 0
# print("-"*20)
# print(items[5])

def subtract_two_numbers(a: int, b: int):
    try:
        return a - b
    except TypeError as error:
        return f"Ooops, avem o eroare: {error}."
    # else:
    #     print(f"Operația a funcționat, rezultatul tău: {result}")
    # finally:
    #     print("Execuția codului s-a încheiat.")


print(subtract_two_numbers(5, 2))
print("-"*20)
result = subtract_two_numbers("Felix", 4)
print(result)

# print(5 / 0)
division = 5 / 0

# Putem trata mai multe erori concomitent
try:
    division
except ZeroDivisionError:
    print("Nu se pot face împărțiri la 0.")
except TypeError:
    print("Încerci să faci o operație cu două tipuri de date diferite.")
else:
    print("Operația a reușit.")
