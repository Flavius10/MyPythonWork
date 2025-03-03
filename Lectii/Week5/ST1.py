"""
Modele de Proiectare Software (Software Design Pattenrs)

Un model de proiectare oferă un set de reguli și principii pentru structurarea și organizarea codului, astfel încât să fie flexibil, ușor de înțeles, ușor de întreținut și de extins; este o soluție generală și recurentă pentru o problemă comună în proiectarea software-ului.

Există 3 mari tipuri de modele:
  1. Creaționale
    - Se concentrează pe procesul de creare a obiectelor într-un mod flexibil și eficient;
    - Ex.: Singleton, Abstract Method, Abstract Factory.
  2. Structurale
    - Se concentrează pe organizarea realațiilor dintre obiecte și clase;
    - Ex.: Adapter, Composite, Proxy.
  3. Comportamentale
    - Se concentrează pe comunicarea și interacțiunea între obiecte și clase;
    - Ex.: Observer, Strategy, Template Method.
"""
# Exemple de Modele Creaționale

# Singleton - o clasă pentru a asigura existența unei singure instanțe a unui manager de construcție
class ConstructionManager:
    _instance = None

    @staticmethod
    def get_instance():
        if not ConstructionManager._instance:
            ConstructionManager._instance = ConstructionManager()
            return ConstructionManager._instance

    def start_construction(self):
        print("Construcția Casei a început.")

# Factory Method - o fabrică de materiale de construcție pentru a crea diverse tipuri de materiale
class ConstructionMaterialFactory:
    def create_material(self, material_type: str):
        if material_type == "cărămidă":
            return Brick()
        elif material_type == "beton":
            return Concrete()
        elif material_type == "lemn":
            return Wood()

class Brick:
    print("Material cărămidă.")

class Concrete:
    print("Material beton.")

class Wood:
    print("Material lemnos.")

# Abstract Factory - o fabrică de mobilă care produce mobilier potrivit pentru diverse stiluri arhitecturale
class FurnitureFactory:
    def create_chair(self):
        pass

    def create_table(self):
        pass

class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self):
        print("Am creat un scaun modern.")

    def create_table(self):
        print("Am creat o masă modernă.")

class VictorianFurnitureFactory(FurnitureFactory):
    def create_chair(self):
        print("Am creat un scaun victorian.")

    def create_table(self):
        print("Am creat o masă victoriană.")


# Modele Structurale

# Adapter - un adaptor pentru a transforma materialele de construcție vechi în formate compatibile cu noile tehnologii de construcție
class ConstructionAdapter:
    def __init__(self, old_material):
        self._old_material = old_material

    def convert(self):
        print(f"Se convertește {self._old_material} într-unul nou.")

# Composite - un șablon care permite gesionarea grupurilor de materiale ca și cum ar fi unul singur
class ConstructionGroup:
    def __init__(self):
        self.materials = []

    def add_material(self, material):
        self.materials.append(material)

    def remove_material(self, material):
        self.materials.remove(material)

    def construct(self):
        print(f"Materiale deținute: {self.materials}")

# Proxy - un intermediar între arhitect și constructor pentru a gestiona procesul de construcție
class ConstructionProxy:
    def __init__(self, architect):
        self.architect = architect

    def request_construction(self):
        print("Putem da start la construcție.")


# Modele Comportamentale

# Observer - o clasă care notifică diferite părți implicate în procesul construcției despre stadiul lucrărilor
class ConstructionStatus:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observer(self, observer):
        print(f"{observer} a fost notificat de status-ul lucrărilor: în execuție.")

# Strategy - diverse strategii de construcție pe baza cerințelor și a condițiilor specifice
class ConstructionStrategy:
    def construct(self):
        pass

class FastConstructionStrategy(ConstructionStrategy):
    def construct(self):
        print("Se construiește folosing metoda rapidă.")

class QualityConstructionStrategy(ConstructionStrategy):
    def construct(self):
        print("Se construiește folosind metoda calitativă.")

# Template Method - un șablon de construcție care definelte pașii comuni și permite implementarea detaliilor specifice în clasele derivate
class ConstructionProcessTemplate:
    def construct(self):
        self._prepare_site()
        self._build_foundation()
        self._construct_walls()
        self._install_roof()
        self._finish()

    def _prepare_site(self):
        print("Se pregătește terenul...")

    def _build_foundation(self):
        print("Turnăm fundația...")

    def _construct_walls(self):
        print("Se ridică pereții...")

    def _install_roof(self):
        print("Se montează acoperișul...")

    def _finish(self):
        print("Finalizăm construcția...")
        print("-"*20)
        print("Construcția este finalizată.")


# Exemplu de utilizare
construction_manager = ConstructionManager().get_instance()

material_factory = ConstructionMaterialFactory()
brick = material_factory.create_material("cărămidă")
concrete = material_factory.create_material("beton")
wood = material_factory.create_material("wood")
print("="*30)

modern_furniture_factory = ModernFurnitureFactory()
victorian_furniture_factory = VictorianFurnitureFactory()
modern_furniture_factory.create_chair()
modern_furniture_factory.create_table()
victorian_furniture_factory.create_chair()
victorian_furniture_factory.create_table()
print("="*30)

construction_adapter = ConstructionAdapter("material vechi")
construction_adapter.convert()

construction_group = ConstructionGroup()
construction_group.add_material("cărămidă")
construction_group.add_material("beton")
construction_group.add_material("lemn")
construction_group.construct()

architect = "Arhitect"
construction_proxy = ConstructionProxy(architect)
construction_proxy.request_construction()
print("="*30)

construction_status = ConstructionStatus()
construction_status.add_observer("arhitect")
construction_status.add_observer("proprietar")
construction_status.add_observer("constructor")
construction_status.notify_observer("Arhitect")

# fast_construction_strategy = FastConstructionStrategy()
quality_construction_strategy = QualityConstructionStrategy()
# fast_construction_strategy.construct()
quality_construction_strategy.construct()

construction_process = ConstructionProcessTemplate()
construction_process.construct()
