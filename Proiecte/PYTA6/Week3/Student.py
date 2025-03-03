class Student:

    def __init__(self, nume: str, varsta: int, specializare: str, *note, media = None):
        self.nume = nume
        self.varsta = varsta
        self.specializare = specializare
        self.note = note
        self.media = media

    def calculeaza_medie(self):
        if not len(self.note) != 0:
            return f"Elevul {self.nume} nu are note, trebuie notat"

        self.media = round(float(sum(self.note) / len(self.note)), 2)
        return f"Elevul {self.nume} are media {self.media}"

    def afiseaza_detalii(self):
        return f"Nume: {self.nume}, Varsta: {self.varsta}, specializare: {self.specializare}, media: {self.media}"

    def este_promovat(self):
        if not self.media >= 5.0:
            return f"Din pacate nu ai promovat avand media {self.media}, iar media de admitere fiind 5.0"

        return f"Ai promovat cu media {self.media}. Felicitari!"



