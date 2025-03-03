class ToDoList:
    def __init__(self, todo: dict):
        self.todo = todo

    def adauga_task(self, nume: str, descriere: str):
        self.todo[nume] = descriere
        print(f"Am adaugat {nume} si trebuie facut {descriere}")

    def finalizează_task(self, nume: str):
        del self.todo[nume]
        print(f"Am sters sarcina cu numele {nume}")

    def afișează_todo_list(self):
        for element in self.todo:
            print(element)

    def afișează_detalii_suplimentare(self, nume_task: str):
        if not nume_task in self.todo:
            intrebare = input("Doriti sa adaugati respectivul task?(da/nu): ")
            if intrebare == "nu":
                print("La revedere!")
            elif intrebare == "da":
                detalii = input("Detaliile taskului sunt: ")
                self.todo[nume_task] = detalii
                print("Date salvate in dictionar")



todolist = ToDoList({})
todolist.adauga_task("Fa aia", "Asa")
todolist.afișează_todo_list()
todolist.afișează_detalii_suplimentare("Merg la alergat")

