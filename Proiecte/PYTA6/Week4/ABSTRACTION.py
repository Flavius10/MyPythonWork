from abc import ABC, abstractmethod


#Interface
class FormaGeometrica(ABC):
    PI = 3.14

    @abstractmethod
    def aria(self):
        pass

    @abstractmethod  #decorator
    def descrie(self):
        pass


class Dreptunghi(FormaGeometrica):

    def __init__(self, l, la):
        self.l = l
        self.la = la

    def aria(self):
        return self.l * self.la

    def descrie(self):
        print("Cel mai probabil am colturi")


class Cerc(FormaGeometrica):
   def __init__(self, r):
       self.r = r

   def aria(self):
       return FormaGeometrica.PI * self.r * self.r

   def descrie(self):
       print("Cel mai  probabil nu am colturi")


# dreptungi = Dreptunghi(10, 20)
# print(dreptungi.aria())
# dreptungi.descrie()
#
# cerc = Cerc(10)
# print(cerc.aria())
# cerc.descrie()
