import json
from database import create_database
from flask import Flask, render_template, Response
from Crud.users_crud import UsersCrud
from Crud.products_crud import ProductsCrud
from Crud.orders_crud import OrdersCrud

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    # return {"mesaj": "Hellow PYTA 6!"}
    return render_template("register.html")


"""API end-points USERS"""


# GET all Users
@app.route("/users", methods=["GET"])
def get_all_users():
    user_crud = UsersCrud()
    try:
        users = user_crud.read()
    except Exception as exc:
        return Response(response=f"Servers Error: {exc}", status=500)
    if users:
        return Response(response=json.dumps(users), status=200)
    return Response(response= f"Nu avem utilizatori in baza de date", status=404)


# GET Users by id
@app.route("/users/<user_id>", methods=["GET"])
def get_users_by_id(user_id):
    user_crud = UsersCrud()
    try:
        users = user_crud.read(user_id)
    except Exception as exc:
        return Response(response=f"Servers Error: {exc}", status=500)
    if users:
        return Response(response=json.dumps(users), status=200)
    return Response(response=f"Nu avem utilizatorul in baza noastra de date", status=404)


# ADD User
@app.route("/users/add", methods=["POST"])
def add_user():
    user_crud = UsersCrud()
    date_intrare = {
        "id": 2,
        "username": "Flavius",
        "password": "Flavius10",
        "email": "flaviusa1010@gmail.com",
        "is_logged": True
    }
    try:
        users = user_crud.create(date_intrare)
    except Exception as exc:
        return Response(response=f"Servers Error: {exc}", status=500)
    if users:
        return Response(response=f"Utilizatorul a fost adaugat: {json.dumps(users)}", status=200)
    return Response(response=f"Not found", status=404)


# UPDATE User
@app.route("/users/update/<userid>", methods=["PUT", "PATCH"])
def update_user(userid):
    user_crud = UsersCrud()
    date_update = {
        "id": userid,
        "username": "Flavius",
        "password": "Flavius10",
        "email": "flaviusa1010@gmail.com",
        "is_logged": True
    }
    try:
        users = user_crud.update(date_update)
    except Exception as exc:
        return Response(response=f"Servers Error: {exc}", status=500)
    if users:
        return Response(response=f"Utilizatorul a fost upgradat: {json.dumps(users)}", status=200)
    return Response(response=f"Not found", status=404)


# DELETE User
@app.route("/users/delete/<userid>", methods=["DELETE"])
def delete_user(userid):
    user_crud = UsersCrud()
    try:
        users = user_crud.delete(userid)
    except Exception as exc:
        return Response(response=f"Servers Error: {exc}", status=500)
    if users:
        return Response(response=f"Utilizatorul a fost sters", status=200)
    return Response(response=f"Not found", status=404)


"""API end-points PRODUCTS"""


# GET ALL PRODUCTS
@app.route("/products", methods=["GET"])
def get_all_products():
    products_crud = ProductsCrud()
    try:
        products = products_crud.read()
    except Exception as exc:
        return Response(response=f"Servers Error: {exc}", status=500)
    if products:
        return Response(response=json.dumps(products), status=200)
    return Response(response= f"Nu avem produse in baza de date", status=404)


# GET PRODUCTS BY ID
@app.route("/products/<productid>", methods=["GET"])
def get_products_by_id(productid):
    products_crud = ProductsCrud()
    try:
        products = products_crud.read(productid)
    except Exception as exc:
        return Response(response=f"Servers Error: {exc}", status=500)
    if products:
        return Response(response=json.dumps(products), status=200)
    return Response(response=f"Nu avem produsul in baza noastra de date", status=404)


# ADD PRODUCTS
@app.route("/products/add", methods=["POST"])
def add_product():
    product_crud = ProductsCrud()
    date_intrare = {
        "product_id": 2,
        "product_name": "Telefon",
        "ingredients": "Metal",
        "weight": "6 inch",
        "price": 4040,
        "available_quantity": 20
    }
    try:
        products = product_crud.create(date_intrare)
    except Exception as exc:
        return Response(response=f"Servers Error: {exc}", status=500)
    if products:
        return Response(response=f"Produsul a fost adaugat: {json.dumps(products)}", status=200)
    return Response(response=f"Not found", status=404)


# UPDATE PRODUCTS
@app.route("/products/update/<productsid>", methods=["PUT", "PATCH"])
def update_products(productsid):
    products_crud = ProductsCrud()
    date_update = {
        "product_id": productsid,
        "product_name": "Telefo",
        "ingredients": "Metal",
        "weight": "6 inch",
        "price": 4040,
        "available_quantity": 20
    }
    try:
        products = products_crud.update(date_update)
    except Exception as exc:
        return Response(response=f"Servers Error: {exc}", status=500)
    if products:
        return Response(response=f"Produsul a fost upgradat: {json.dumps(products)}", status=200)
    return Response(response=f"Not found", status=404)


# DELETE PRODUCTS
@app.route("/products/delete/<products_id>", methods=["DELETE"])
def delete_products(products_id):
    product_crud = ProductsCrud()

    try:
        products = product_crud.delete(products_id)
    except Exception as exc:
        return Response(response=f"Servers Error: {exc}", status=500)
    if products:
        return Response(response=f"Produsul a fost sters", status=200)
    return Response(response=f"Not found", status=404)


"""API end-points ORDERS"""


# GET ALL ORDERS
@app.route("/orders", methods=["GET"])
def get_all_orders():
    order_crud = OrdersCrud()
    try:
        orders = order_crud.read()
    except Exception as exc:
        return Response(response=f"Servers Error: {exc}", status=500)
    if orders:
        return Response(response=json.dumps(orders), status=200)
    return Response(response= f"Nu avem orders in baza de date", status=404)


# GET ORDERS BY ID
@app.route("/orders/<order_id>", methods=["GET"])
def get_orders_by_id(order_id):
    order_crud = OrdersCrud()
    try:
        order = order_crud.read(order_id)
    except Exception as exc:
        return Response(response=f"Servers Error: {exc}", status=500)
    if order:
        return Response(response=json.dumps(order), status=200)
    return Response(response=f"Nu avem produsul in baza noastra de date", status=404)


# ADD ORDERS
@app.route("/orders/add", methods=["POST"])
def add_orders():
    order_crud = OrdersCrud()
    date_intrare = {
        "order_id": 1,
        "user_id": 2
    }
    try:
        orders = order_crud.create(date_intrare)
    except Exception as exc:
        return Response(response=f"Servers Error: {exc}", status=500)
    if orders:
        return Response(response=f"Utilizatorul a fost adaugat: {json.dumps(orders)}", status=200)
    return Response(response=f"Not found", status=404)


# UPDATE ORDERS
@app.route("/orders/update/<order_id>", methods=["PUT", "PATCH"])
def update_order(order_id):
    orders_crud = OrdersCrud()
    date_update = {
        "order_id": order_id,
        "user_id": 2
    }
    try:
        orders = orders_crud.update(date_update)
    except Exception as exc:
        return Response(response=f"Servers Error: {exc}", status=500)
    if orders:
        return Response(response=f"Produsul a fost upgradat: {json.dumps(orders)}", status=200)
    return Response(response=f"Not found", status=404)


# DELETE ORDERS
@app.route("/orders/delete/<order_id>", methods=["DELETE"])
def delete_orders(order_id):
    order_crud = OrdersCrud()

    try:
        orders = order_crud.delete(order_id)
    except Exception as exc:
        return Response(response=f"Servers Error: {exc}", status=500)
    if orders:
        return Response(response=f"Produsul a fost sters", status=200)
    return Response(response=f"Not found", status=404)


if __name__ == '__main__':
    create_database()
    app.run(debug=True, port=700)

