"""In cadrul acestui fisier vom creea metodele crud pentru tabela Products"""

from Crud.abstract_crud import CrudABC


class ProductsCrud(CrudABC):

    def create(self, date_intrare):
        query = "INSERT INTO Products(product_id, product_name, ingredients, weight, price, available_quantity" \
                "VALUES (:product_id, :product_name, :ingredients, :weight, :price, :available_quantity)"

        cursor = self.connection.cursor()
        cursor.execute(query, date_intrare.__dict__)
        self.connection.commit()

    def read(self, id=None):
        if id is None:
            query = "SELECT * FROM Products"

            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()

            date_produse = cursor.fetchall()
            lista_produs = []

            for produs in date_produse:
                lista_produs.append({
                    "product_id": produs[0],
                    "product_name": produs[1],
                    "ingredients": produs[2],
                    "weight": produs[3],
                    "price": produs[4],
                    "available_quantity": produs[5]
                })

            return lista_produs
        else:
            query = "SELECT * FROM Products WHERE id = :id"

            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()

            date_produse = cursor.fetchall()
            lista_produs = []

            for produs in date_produse:
                lista_produs.append({
                    "product_id": produs[0],
                    "product_name": produs[1],
                    "ingredients": produs[2],
                    "weight": produs[3],
                    "price": produs[4],
                    "available_quantity": produs[5]
                })

            return lista_produs

    def update(self, date_update):
        query = "UPDATE Products SET product_id = :product_id, product_name = :product_name," \
                " ingredients = :ingredients"\
                "weight = :weight, price = :price, available_quantity = :available_quantity" \
                " WHERE product_id = :product_id"

        cursor = self.connection.cursor()
        cursor.execute(query, date_update.__dict__)
        self.connection.commit()

    def delete(self, id):
        query = "DELETE FROM Products WHERE product_id = ?"

        cursor = self.connection.cursor()
        cursor.execute(query, (id, ))
        self.connection.commit()

        return bool(cursor.rowcount)
