"""
Topic principal: Cicluri repetitive („for” și „while”)
"""

# FOR
# Element iterabil = Colecție de date
# Sintaxă generală:
# for element in elements:
#   do_someting_with(element)
# else:
#   do_another_thing()
# names_list = ["Ioan", "Radu", "Roxana", "Bogdan", "Felix"]
# names_tuple = tuple(names_list)
# names_set = set(names_list)
# names_dict = {
#     "name1": "Ioan",
#     "name2": "Radu",
#     "name3": "Roxana",
#     "name4": "Bogdan",
#     "name5": "Felix"
# }
# By default iterează prin chei, nu prin valori
# Dacă vrem să iterăm prin valori trebuie să folosim nume_dicționar.values()
# Dacă vrem să iterăm atât prin chei, cât și prin valori folosim nume_dicționar.items()
# for name in names_dict.values():
#     print(name)
# for key, value in names_dict.items():
#     print(f"Cheie: {key}, Valoare: {value}")

# for name in names_list:
#     print(name)
# else:
#     print("-"*20)
#     print("Iterația s-a încheiat.")

# print("Elementele iterate din listă:")
# for name in names_list:
#     print(name)

# print("Elementele iterate din set:")
# for name in names_set:
#     print(name)

# metoda „range(start, stop, step)” - exact ca la string/list slicing
# 2 cuvinte rezervate importante: „continue” și „break”
# nums = list(range(1, 11))
# number_of_elements = range(1, len(names_list)+1)
#
# for item in enumerate(names_list):
#     print(item)
# else:
#     print("-"*20)
# for index, item in enumerate(names_list):
#     print(f"Item {item} at position {index+1}.")

# for num in nums:
#     if num % 2 != 0:
#         continue
#     print(num)
# for num in nums:
#     if num == 8:
#         break
#     print(num)
# for name in range(len(names_list)):
#     print(name)

# Ciclu repetitiv cu variabilă anonimă
# for _ in names_list:
#     print("Hello world!")


# WHILE
# while condiție=True:
#   do_someting()
#   something_to_increment ++
# else:
#   do_another_thing()
# Ca o precauție, NU folosim `continue` întrucât poate genera o buclă infinită
# i = 1
# while i <= 10:
#     if i == 9:
#         break
#     print(f"Condiția se îndeplinește, i este egal cu {i}")
#     i += 1  # echivalent cu i = i + 1
# else:
#     print("Condiția nu s-a mai îndeplinit.")

# flag = True
# counter = 1
# while flag:
#     if counter == 4:
#         flag = False
#     print("Hello world!")
#     counter += 1
