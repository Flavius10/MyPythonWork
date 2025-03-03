from ABSTRACTION import FormaGeometrica


class Patrat(FormaGeometrica):
    def __init__(self, latura):
        self.latura = latura

    def aria(self):
        return self.latura * self.latura

    def descrie(self):
        print("Am toate laturile egale")


# patrat = Patrat(10)
# print(patrat.aria())
# patrat.descrie()
