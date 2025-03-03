from ABSTRACTION import FormaGeometrica


class Patrat(FormaGeometrica):

    def __init__(self, latura):
        self.__latura = latura

    @property
    def latura(self):
        return self.__latura

    @latura.getter
    def latura(self):
        print(f"Latura are {self.__latura} cm")
        return self.__latura

    @latura.setter
    def latura(self, latura):
        print(f"Noua latura are {latura} cm")
        self.__latura = latura

    @latura.deleter
    def latura(self):
        print("Am sters lungimea laturii")
        del self.__latura

    def aria(self):
        print("Aria:", end="")
        return self.__latura * self.__latura

    def descrie(self):
        print("Eu am colturi")


# patrat = Patrat(10)
# patrat.latura
# patrat.latura = 12
# patrat.latura
# del patrat.latura


class Cerc(FormaGeometrica):
    def __init__(self, raza):
        self.__raza = raza

    @property
    def raza(self):
        return self.__raza

    @raza.getter
    def raza(self):
        print(f"Raza cercului este {self.__raza}")
        return self.__raza

    @raza.setter
    def raza(self, raza):
        print(f"Cercul are raza noua egala cu {raza}")
        self.__raza = raza

    @raza.deleter
    def raza(self):
        del self.__raza

    def aria(self):
        return FormaGeometrica.PI * self.__raza * self.__raza

    def descrie(self):
        print("Eu nu am colturi")


# cerc = Cerc(10)
# cerc.raza
# cerc.raza = 20
# cerc.raza
# print(cerc.aria())
