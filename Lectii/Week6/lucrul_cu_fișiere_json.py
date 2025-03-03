import json
import os


current_dir = os.getcwd()
json_data = os.path.join(current_dir, "data.json")

# Citirea datelor dintr-un fișier JSON (parsare / deserializare)
with open(json_data, 'r') as file:
    print(type(json_data))
    data = json.load(file)
    print(type(data))

# Scrierea datelor într-un fișier JSON / serializare
data = {
    "nume": "Felix C. Pericică",
    "vârsta": 29
}

with open(json_data, 'a', encoding='utf-8') as file:
    json.dump(data, file)
