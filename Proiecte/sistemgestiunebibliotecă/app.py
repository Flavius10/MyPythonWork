from helpers.gestiune import Gestiune

gestionare = Gestiune()
# gestionare.adauga_carte("Ion", "Flavius", 13353)
# gestionare.adauga_carte("Pinochio", "Flavius", 183295)
# gestionare.imprumuta_carte("Ion", "Flavius")
# gestionare.imprumuta_carte("Pinochio", "Flavius")
# gestionare.returneaza_carte("Pinochio")
# gestionare.elemina_carte("Ion")

# gestionare.afiseaza_carti_imprumutate()
# gestionare.afiseaza_carti_disponibile()

gestionare.inregistreaza_membru("Flavius", "BN4327")
gestionare.afiseaza_membri()
gestionare.sterge_membru("Flavius")

