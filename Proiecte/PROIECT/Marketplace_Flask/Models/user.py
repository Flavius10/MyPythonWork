from exceptions import ValidationError
from validate_email import validate_email


class User:
    def __init__(self, id, username, password, email, is_logged):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
        self.is_logged = is_logged

    def validate(self):
        self.__validate_username()
        self.__validate_email()
        self.__validate_password()

    def __validate_username(self):
        special_caracters = ",.<>/?&*%$#^@';:[{}]\|_-=+!`~"
        if any([c in special_caracters for c in self.username]):
            raise ValidationError("Numele utilizatorului contine caractere speciale!")

    def __validate_email(self):
        is_valid = validate_email(self.email)
        return is_valid

    def __validate_password(self):
        special_caracters = ",.<>/?&*%$#^@';:[{}]\_-=+!`~"
        if len(self.password) < 8:
            raise ValidationError("Parola trebuie sa fie din minim 8 caractere")
        if not any([c in special_caracters for c in self.password]):
            raise ValidationError("Parola trebuie sa contina minim un caracter special")
        numbers = "0123456789"
        if not any([c in numbers for c in self.password]):
            raise ValidationError("Parola trebuie sa contina minim o cifra")