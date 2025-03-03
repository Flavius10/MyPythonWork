"""
Iteratori, Generatori, Manageri de Context și Decoratori

Eficiență temporală - cât de costisitor este codul dpdv al timpului de execuție
Eficiență spațială - cât de costisitor este codul dpdv al memoriei

Un Iterator este un obiect care permite parcurgerea secvențială a unei colecții de elemente, fără a expune detaliile de implementare ale colecției.

Un Generator este o metodă specială în Python care produce o secvență de valori pe măsură ce este iterată, în loc să le genereze în întregime înainte de a le returna.

Managerii de Context sunt folosiți pentru a gestiona resursele, cum ar fi fișierele, conexiunile la baze de date, sau alte obiecte care necesită o deschidere și închidere adecvată. Aceștia se asigură că resursele sunt eliberate în mod corespunzător chiar și în cazul apariției unor excepții.

Decoratorii sunt funcții speciale care iau o altă funcție ca argument și adaugă comportament suplimentar acelei funcții fără a o modifica în mod direct. Decoratorii sunt utili pentru a modifica comportamentul unei funcții fără a repeta codul în mai multe locuri.
"""
# Iterator
class BookListOrder:
    def __init__(self, book_order: int):
        self.book_order = book_order
        self.current_book = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_book <= self.book_order:
            book = self.current_book
            self.current_book += 1
            return book


fructe = ["cireșe", "vișine", "pepene", "mere"]
iterator_de_fructe = iter(fructe)

while True:
    try:
        element = next(iterator_de_fructe)
        print(element)
    except StopIteration:
        break

# Generator
def countdown(n):
    while n > 0:
        yield n
        n -= 1

# Ctx Manager syntax
# with method() as alias:
#   do_something_with_alias()
def rent():
    with open('rent_actions.txt', 'r', encoding='utf-8', errors='ignore') as file:
        rent_actions = file.read()
        print(rent_actions)


# Decorator
def mailbox_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"[Received] {result}"

    return wrapper

def send_letter_without_decorator(message):
    return f"Letter: {message}"


@mailbox_decorator
def send_letter_with_decorator(message):
    return f"Letter: {message}"


if __name__ == "__main__":
    rent()
