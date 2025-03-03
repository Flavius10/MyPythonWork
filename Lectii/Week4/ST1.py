"""
Pilonii Programării Orientate pe Obiecte:
  1. Moștenirea (Inheritance);
  2. Abstractizarea (Abstraction);
  3. Încapsularea (Encapsulation);
  4. Polimorfismul (Polymorphism).

Moștenirea este procedeul prin care o clasă, denumită clasă copil, sau clasă derivată,
moștenește (preia) atributele și metodele unei alte clase, denumită clasă părinte.
Clasa derivată poate avea propriile atribute și metode.

Abstractizarea este procesul de definire a unei clase abstracte care nu poate fi
instanțiată și servește drept șablon pentru alte clase.
Clasă abstractă: poate conține metode abstracte (fără implementare) și metode concrete.
Interfață: strict o colecție de metode abstracte (fără implementare) și nu poate
conține atribute sau metode concrete.
                   
Încapsularea se referă la ambalarea datelor și metodelor relevante într-o singură
entitate (clasă) și la ascunderea detaliilor interne ale obiectului. Scopul încapsulării
este de a ascunde detalii de implementare și de a proteja integritatea datelor unei clase.
Există anumite convenții care determină accesibilitatea atributelor și metodelor în cadrul
unei clase și a claselor derivate, și acestea sunt modificatorii de acces:
  * public - un atribut sau o metodă normală;
  * protejat - se folosește de convenția de notare „_nume”;
  * private - convenția de notare cu „__nume”.

Polimorfismul se referă la capacitatea unui obiect de a manifesta comportamente diferite
în funcție de contextul în care este utilizat.                                                             
Două concepte cheie: suprascrierea (overriding) și supraîncărcarea (overloading).
By default, în Python nu există overloading, doar overriding; totuși, există soluții
alternative: folosind metoda „super()” sau un decorator.
"""
# Exemplu de aplicare al Moștenirii
# class Vehicul:
#     def __init__(self, marca: str, an: int):
#         self.marca = marca
#         self.an = an
#
#     def afiseaza_detalii(self):
#         print(f"Marca: {self.marca}.")
#         print(f"An: {self.an}.")
#
#
# class Car(Vehicul):
#     def __init__(self, marca: str, an: int, nr_ulei: int):
#         super().__init__(marca, an)
#         self.nr_ulei = nr_ulei
#
#     def schimba_ulei(self, nr_nou: int):
#         self.nr_ulei = nr_nou
#
#
# class Camioneta(Car):
#     def __init__(self, marca: str, an: int, nr_ulei: int, capacitate: int):
#         super().__init__(marca, an, nr_ulei)
#         self.capacitate = capacitate
#
#     def afiseaza_detalii(self):
#         super().afiseaza_detalii()
#         print(f"Capacitate: {self.capacitate} tone.")


# ford = Vehicul("Ford", 2022)
# ford.afiseaza_detalii()
# print("-"*20)
#
# toyota = Car("Toyota", 2021, 215_000)
# toyota.afiseaza_detalii()
# toyota.schimba_ulei(225_000)
# print(f"Mașina va trebui să schimbe uleiul la {toyota.nr_ulei} km.")
# print("-"*20)
#
# camioneta = Camioneta("Volvo", 2020, 100_000, 4)
# camioneta.afiseaza_detalii()


# Exemplu aplicat de Abstractizare
# from abc import ABC, abstractmethod
#
#
# # ABC = Abstract Base Class
# class Vehicul(ABC):
#     def porneste(self):
#         print("Mașina a pornit.")
#
#     @abstractmethod # decorator
#     def accelereaza(self):
#         pass
#
#     @abstractmethod
#     def franeaza(self):
#         pass
#
#
# class Masina(Vehicul):
#     def accelereaza(self):
#         print("Mașina accelerează.")
#
#     def franeaza(self):
#         print("Mașina frânează.")
#
#
# masina = Masina()
# masina.porneste()
# masina.accelereaza()


# class Masina:
#     def __init__(self, marca: str, an: int, pret: int):
#         self._marca = marca
#         self._an = an
#         self._pret = pret
#
# #     Getter, Setter, Deleter
# #     Getter = setez marca ca fiind o proprietate accesibilă din exterior
#     @property
#     def marca(self):
#         return self._marca
#
#     @property
#     def pret(self):
#         return
#
#     # Getter = setez pretul ca fiind o proprietate accesibilă din exterior
#     @pret.getter
#     def pret(self):
#         return f"Prețul mașinii este de {self._pret}."
#
#     # Setter-ul este folosit pentru a seta o proprietate din exteriorul clasei
#     @pret.setter
#     def pret(self, pret_nou: int):
#         if pret_nou > 0:
#             self._pret = pret_nou
#         else:
#             print("Prețul trebuie să fie mai mare decât 0.")
#
#     # Deleter-ul se folosește pentru a șterge atributul
#     @pret.deleter
#     def pret(self):
#         del self._pret
#
#
# masina = Masina("Toyota", 2022, 25_000)
# print(masina.pret)
# masina.pret = 22_000
# print(masina.pret)
# del masina.pret
# print(masina.pret)
