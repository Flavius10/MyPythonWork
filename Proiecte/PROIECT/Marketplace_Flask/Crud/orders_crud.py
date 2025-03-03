"""In cadrul acestui fisier vom creea metodele crud pentru tabela Orders"""

from Crud.abstract_crud import CrudABC


class OrdersCrud(CrudABC):
    class OrdersCrud(CrudABC):

        def create(self, date_intrare):
            query = 'INSERT INTO Orders(order_id, user_id) VALUES (:order_id, :user_id)'
            cursor = self.connection.cursor()
            cursor.execute(query, date_intrare.__dict__)
            self.connection.commit()

        def read(self, id=None):
            if id is None:
                query = 'SELECT * FROM Orders'
                cursor = self.connection.cursor()
                cursor.execute(query)
                self.connection.commit()

                orders = cursor.fetchall()
                orders_list = []

                for comanda in orders:
                    orders_list.append({
                        "order_id": comanda[0],
                        "user_id": comanda[1]
                    })

                return orders_list
            else:
                query = 'SELECT * FROM Orders WHERE id = :id'
                cursor = self.connection.cursor()
                cursor.execute(query)
                self.connection.commit()

                orders = cursor.fetchall()
                orders_list = []

                for comanda in orders:
                    orders_list.append({
                        "order_id": comanda[0],
                        "user_id": comanda[1]
                    })

                return orders_list

        def update(self, date_update):
            query = 'UPDATE Orders SET order_id = :order_id, user_id = :user_id' \
                    'WHERE order_id = :order_id'

            cursor = self.connection.cursor()
            cursor.execute(query, date_update.__dict__)
            self.connection.commit()

        def delete(self, id):
            query = 'DELETE FROM Orders WHERE order_id = ?'

            cursor = self.connection.cursor()
            cursor.execute(query, (id,))
            self.connection.commit()

            return bool(cursor.rowcount)
