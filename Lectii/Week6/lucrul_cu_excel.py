import os
import pandas as pd


# Citește un fișier XLSX
file_location = os.getcwd()
df = pd.read_excel("note.xlsx")

# Accesăm diferite coloane
# print(df['Medie'])
print(f"Media pe clasă: {df['Medie'].mean()}")
