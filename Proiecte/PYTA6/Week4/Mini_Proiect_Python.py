class Masina:
    def __init__(self, model: str, viteza_maxima: int):
        self.model = model
        self.marca = "BMW"
        self.viteza_maxima = viteza_maxima
        self.viteza_actuala = 0
        self.culoare = 'gri'
        self.culori_disponibile = {'Portocaliu', 'Rosu', 'Verde', 'Albastru', 'Mov', 'Galben'}
        self.inmatriculata = False

    def descrie(self):
        print(f"Marca: {self.marca}")
        print(f"Viteza actuala: {self.viteza_actuala}")
        print(f"Viteza maxima: {self.viteza_maxima}")
        print(f"Culoare: {self.culoare}")
        print(f"Model: {self.model}")
        print(f"Inmatriculata: {self.inmatriculata}")

    def inmatriculare(self):
        self.inmatriculata = True
        print("Masina a fost inmatriculata")

    def vopseste(self, culoare: str):
            if culoare in self.culori_disponibile:
                self.culoare = culoare
                print(f"Masina e acum de culoarea {culoare}")
            else:
                raise NotImplementedError("Nu exista culoarea ceruta")

    def franeaza(self):
        self.viteza_actuala = 0
        print(f"Masina a franat si acum a scazut viteza la {self.viteza_actuala}")

    def acceleraza(self, viteza: int):
        if viteza < 0:
            raise NotImplementedError("Viteza trebuie sa fie pozitiva")
        elif self.viteza_maxima < viteza:
            self.viteza_actuala = self.viteza_maxima
            print(f"Masina a accelerat la {self.viteza_actuala}")
        else:
            self.viteza_actuala = viteza
            print(f"Masina a accelerat la {self.viteza_actuala}")


masina = Masina("Serria 5", 250)
masina.descrie()
masina.inmatriculare()
masina.vopseste('Mov')
masina.acceleraza(40)
masina.franeaza()


