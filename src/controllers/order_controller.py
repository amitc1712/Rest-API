from flask import request, jsonify
from models.category import db
from models.order import OrderModel, order_schema, orders_schema


# Create new order
def add_order():
    OrderID = request.json["OrderID"]
    CustomerID = request.json["CustomerID"]
    EmployeeID = request.json["EmployeeID"]
    Freight = request.json["Freight"]
    OrderDate = request.json["OrderDate"]
    RequiredDate = request.json["RequiredDate"]
    ShipAddress = request.json["ShipAddress"]
    ShipCity = request.json["ShipCity"]
    ShipCountry = request.json["ShipCountry"]
    ShipName = request.json["ShipName"]
    ShippedDate = request.json["ShippedDate"]
    ShipPostalCode = request.json["ShipPostalCode"]
    ShipRegion = request.json["ShipRegion"]
    ShipVia = request.json["ShipVia"]

    new_order = OrderModel(
        OrderID,
        CustomerID,
        EmployeeID,
        Freight,
        OrderDate,
        RequiredDate,
        ShipAddress,
        ShipCity,
        ShipCountry,
        ShipName,
        ShippedDate,
        ShipPostalCode,
        ShipRegion,
        ShipVia,
    )

    db.session.add(new_order)
    db.session.commit()

    return order_schema.jsonify(new_order)


# Get All Orders
def get_orders():
    all_orders = OrderModel.query.all()
    result = orders_schema.dump(all_orders)
    return jsonify(result)


# Update a Order
def update_order(OrderID):
    order = OrderModel.query.get(OrderID)

    CustomerID = request.json["CustomerID"]
    EmployeeID = request.json["EmployeeID"]
    Freight = request.json["Freight"]
    OrderDate = request.json["OrderDate"]
    RequiredDate = request.json["RequiredDate"]
    ShipAddress = request.json["ShipAddress"]
    ShipCity = request.json["ShipCity"]
    ShipCountry = request.json["ShipCountry"]
    ShipName = request.json["ShipName"]
    ShippedDate = request.json["ShippedDate"]
    ShipPostalCode = request.json["ShipPostalCode"]
    ShipRegion = request.json["ShipRegion"]
    ShipVia = request.json["ShipVia"]

    order.CustomerID = CustomerID
    order.EmployeeID = EmployeeID
    order.Freight = Freight
    order.OrderDate = OrderDate
    order.RequiredDate = RequiredDate
    order.ShipAddress = ShipAddress
    order.ShipCity = ShipCity
    order.ShipCountry = ShipCountry
    order.ShipName = ShipName
    order.ShippedDate = ShippedDate
    order.ShipPostalCode = ShipPostalCode
    order.ShipRegion = ShipRegion
    order.ShipVia = ShipVia

    db.session.commit()

    return order_schema.jsonify(order)
