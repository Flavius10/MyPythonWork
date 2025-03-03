from Week3 import Student
from Student import Student

student1 = Student("Flavius", 17, "Informatica", 10, 10, 10, 10, 8, 9, 10)
print(student1.calculeaza_medie())
print(student1.afiseaza_detalii())
print(student1.este_promovat())

print("-" * 40)

student2 = Student("Gigel", 18, "Fizica", 10, 5, 4, 3, 2, 1, 2)
print(student2.calculeaza_medie())
print(student2.afiseaza_detalii())
print(student2.este_promovat())
