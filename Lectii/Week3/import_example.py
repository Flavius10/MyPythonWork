from ST2 import Masina


dacia = Masina("Dacia", "Logan", 2009, "albă")

print("="*20)
print(f"Mașina mea este o {dacia.marca} {dacia.model}, din anul {dacia.an}, de culoarea {dacia.culoare}.")
print("-"*20)
print(dacia.porneste_motor())
print(dacia.accelereaza(40))
print(dacia.accelereaza(30))
print(dacia.franeaza(30))
print(dacia.accelereaza(60))
print(dacia.franeaza(100))
print(dacia.opreste_motor())
