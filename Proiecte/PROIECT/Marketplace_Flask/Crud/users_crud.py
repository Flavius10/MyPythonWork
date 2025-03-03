"""In cadrul acestui fisier vom creea metodele crud pentru tabela Users"""

from Crud.abstract_crud import CrudABC


class UsersCrud(CrudABC):

    def create(self, date_intrare):
        query = 'INSERT INTO Users(id, username, password, email, is_logged) VALUES ' \
                '(:id, :username, :password, :email, :is_logged)'
        cursor = self.connection.cursor()
        cursor.execute(query, date_intrare.__dict__)
        self.connection.commit()

    def read(self, id=None):
        if id is None:
            query = 'SELECT * FROM Users'
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()

            utilizatori = cursor.fetchall()  # lista de dictionare
            utilizatori_json = []

               #dictionar     lista de dictionare
               #   |                |
               #   |                |
            for utilizator in utilizatori:
                utilizatori_json.append({
                    'id': utilizator[0],
                    'username': utilizator[1],
                    'password': utilizator[2],
                    'email': utilizator[3],
                    'is_logged': utilizator[4]
                })

            return utilizatori_json

        else:

            query = 'SELECT * FROM Users WHERE id = :id'
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()

            utilizatori = cursor.fetchall()  # lista de dictionare
            utilizatori_json = []

            # dictionar     lista de dictionare
            #   |                |
            #   |                |
            for utilizator in utilizatori:
                utilizatori_json.append({
                    'id': utilizator[0],
                    'username': utilizator[1],
                    'password': utilizator[2],
                    'email': utilizator[3],
                    'is_logged': utilizator[4]
                })

            return utilizatori_json

    def update(self, date_update):
        query = 'UPDATE Users SET id = :id, username = :username,' \
                ' password = :password, email = :email, is_logged = :is_logged WHERE id = :id'

        cursor = self.connection.cursor()
        cursor.execute(query, date_update.__dict__)
        self.connection.commit()

    def delete(self, id):
        query = 'DELETE FROM Users WHERE id = ?'

        cursor = self.connection.cursor()
        cursor.execute(query, (id,))
        self.connection.commit()

        return bool(cursor.rowcount)
