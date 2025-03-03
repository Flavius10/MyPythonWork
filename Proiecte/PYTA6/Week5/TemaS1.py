# Singelton

class CarDesigner:
    _instance = None

    @staticmethod
    def get_instance():
        if not CarDesigner._instance:
            return CarDesigner._instance

    def start_byuild(self):
        print("Incepem sa construim masina")

# Factory Method


class CarParts:
    def car_parts(self, parti: str):
        if parti == "Roti":
            return Wheels()
        elif parti == "Usa":
            return Door()


class Wheels:
    pass


class Door:
    pass


car_part = CarParts()
car_part.car_parts("Roti")


#Abstract Factory

class CarType:

    def ani_vechime(self, ani: int):
        pass

    def caroserie(self):
        pass


class ClasicCar(CarType):

    ani_vechi = 0

    def ani_vechime(self, ani: int):
        self.ani_vechi = ani
        print(f"Are {ani} vechime")

    def caroserie(self):
        print(f"Caroserie clasica din anii {2023 - self.ani_vechi}")


class ModernCar(CarType):

    ani_vechi = 0
    def ani_vechime(self, ani: int):
        self.ani_vechi = ani
        print(f"Are {ani} vechime")

    def caroserie(self):
        print(f"Caroserie clasica din anii {2023 - self.ani_vechi}")


masina = ClasicCar()
masina.ani_vechime(40)
masina.caroserie()

print("=" * 30)

masina_noua = ModernCar()
masina_noua.ani_vechime(2)
masina_noua.caroserie()

print("=" * 30)


# Adapter
class CarTunning:
    def __init__(self, motor: str):
        self.motor = motor

    def tuneaza(self, motor):
        print(f"Din motorul {self.motor} se tuneaza la motorul {motor}")
        self.motor = motor


car_tunning = CarTunning("Motor mic")
car_tunning.tuneaza("Motor mare")
print("=" * 30)

# Composite
class Parts:
    def __init__(self):
        self.parts = []

    def add_parts(self, piesa: str):
        self.parts.append(piesa)

    def remove_parts(self, piesa: str):
        self.parts.remove(piesa)

    def construct(self):
        print(f"Avem la dispozitie urmatoarele piese: {self.parts}")


parti = Parts()
parti.add_parts("Usa")
parti.add_parts("Roti")
parti.construct()
print("=" * 30)

# Proxy

class Permission:
    def __init__(self, dessigner: str):
        self.dessigner = dessigner

    def permisiune(self):
        print(f"Putem decora masina, fiind la conducere {self.dessigner}")


permission = Permission("Dessigner")
permission.permisiune()
print("=" * 30)


# Observer
class CarStatus:
    def __init__(self):
        self.sefi = []

    def add_sefi(self, sef: str):
        self.sefi.append(sef)

    def remove_sef(self, sef: str):
        self.sefi.remove(sef)

    def notifica_sefi(self, sef: str):
        print(f"{sef} a fost notificat de progesul constructiei masinii")


car_status = CarStatus()
car_status.add_sefi("Flavius")
car_status.notifica_sefi("Flavius")
print("=" * 30)

# Strategy
class CarConstructionStategy:
    def construct(self):
        pass

class CarConstructionAutomatic(CarConstructionStategy):
    def construct(self):
        print("Masina este construita automat")

class CarConstructionManual(CarConstructionStategy):
    def construct(self):
        print("Masina este construita manual")


car_strategy = CarConstructionAutomatic()
car_strategy.construct()

car_strategy_manual = CarConstructionManual()
car_strategy_manual.construct()
print("=" * 30)


# Template Method

class CarConstructionProcces:

    def construct(self):
        self._prepeare()
        self._build()
        self._get_money()

    def _prepeare(self):
        print("Pregatim proiectul...")

    def _build(self):
        print("Facem masina...")

    def _get_money(self):
        print("Primim banii...")


car_construction_procces = CarConstructionProcces()
car_construction_procces.construct()
