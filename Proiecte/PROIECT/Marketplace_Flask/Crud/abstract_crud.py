"""O clasa abstracta cu metodele crud abstracte"""

from abc import ABC, abstractmethod
from database import get_db_connection


class CrudABC(ABC):
    def __init__(self):
        self.connection = get_db_connection()

    @abstractmethod
    def create(self, date_intrare):
        pass

    @abstractmethod
    def read(self, id=None):
        pass

    @abstractmethod
    def update(self, date_update):
        pass

    @abstractmethod
    def delete(self, id):
        pass




