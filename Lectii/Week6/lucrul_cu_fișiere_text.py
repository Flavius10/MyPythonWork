import os


current_directory = os.getcwd()
file = "text.txt"
path = os.path.join(current_directory, file)

# Deschiderea și citirea conținutului unui fișier text
with open(path, 'r', encoding='utf-8') as file:
    content = file.read()
    # print(content)

# Citirea liniilor și iterarea prin liniile unui fișier
with open(path, 'r', encoding='utf-8') as file:
    # print(file.readline())
    # print("-"*30)
    # print(file.readlines())
    # for line in file:
    #     print(line)
    pass

# Scrierea într-un fișier
# with open(path, 'w') as f:
#     f.write("Hello world!")
# with open(path, 'a') as f:
#     f.write("Hello world!")

logs = os.path.join(current_directory, "logs.txt")

# Exemplu cu log
with open(logs, 'a', encoding='utf-8') as f:
    i = 0
    while i < 19:
        if i % 3 == 0:
            print(f"Logged with {i}", file=f)
        i += 1
