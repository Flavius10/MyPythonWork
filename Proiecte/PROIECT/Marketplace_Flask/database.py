'''
In cadrul acestui fisier am facut setup-ul pentru a crea baza de date.
'''

import sqlite3
db_file = 'produse_patiserie.db'        # am creat calea catre fisierul nostru de baza de date

def get_db_connection(db_path = db_file):
    connection = sqlite3.connect(db_path)
    return connection

def create_database(db_path = db_file):
    connection = sqlite3.connect(db_path)
    create_tables(connection)

def create_tables(connection):
    create_users_table(connection)
    create_products_table(connection)
    create_orders_table(connection)
    create_orderlines_table(connection)


def create_users_table(connection):             # se va scrie in query un script
    query = ''' 
        CREATE TABLE IF NOT EXISTS Users(
        id TEXT NOT NULL PRIMARY KEY,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        email TEXT NOT NULL,
        is_logged INTEGER NOT NULL DEFAULT 0 CHECK (is_logged IN (0, 1))
        )
    '''

    cursor = connection.cursor()
    cursor.executescript(query)
    connection.commit()                         # se apeleaza commit pentru a se incarca in bd


def create_products_table(connection):
    query = ''' 
            CREATE TABLE IF NOT EXISTS Products(
            product_id TEXT NOT NULL PRIMARY KEY,
            product_name TEXT NOT NULL,
            ingredients TEXT NOT NULL,
            weight INTEGER NOT NULL,
            price REAL NOT NULL,
            available_quantity INTEGER NOT NULL DEFAULT 0
            )
            '''
# REAL = FLOAT
    cursor = connection.cursor()
    cursor.executescript(query)
    connection.commit()

def create_orders_table(connection):
    query = ''' 
            CREATE TABLE IF NOT EXISTS Orders (
            order_id TEXT NOT NULL PRIMARY KEY,
            user_id FOREIGN_KEY REFERENCES Users(id)
                )
            '''
    cursor = connection.cursor()
    cursor.executescript(query)
    connection.commit()

def create_orderlines_table(connection):
    query = ''' 
            CREATE TABLE IF NOT EXISTS OrderLines (
            orderline_id FOREIGN_KEY REFERENCES Orders(order_id),
            product_id FOREIGN_KEY REFERENCES Products(product_id),
            quantity INTEGER NOT NULL,
            subtotal REAL NOT NULL
            )
            '''
    cursor = connection.cursor()
    cursor.executescript(query)
    connection.commit()

