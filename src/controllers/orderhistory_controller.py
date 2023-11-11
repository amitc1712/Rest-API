from flask import jsonify
from models.customer import CustomerModel
from models.order import OrderModel


# Order history of a given customer
def get_order_history(CustomerID):
    customer = CustomerModel.query.get(CustomerID)
    if not customer:
        return jsonify({"message": "Customer not found"}), 404

    orders = OrderModel.query.filter_by(CustomerID=CustomerID).all()

    order_history = []
    for order in orders:
        order_history.append(
            {
                "OrderID": order.OrderID,
                "CustomerID": order.CustomerID,
                "EmployeeID": order.EmployeeID,
                "Freight": order.Freight,
                "OrderDate": order.OrderDate,
                "RequiredDate": order.RequiredDate,
                "ShipAddress": order.ShipAddress,
                "ShipCity": order.ShipCity,
                "ShipCountry": order.ShipCountry,
                "ShipName": order.ShipName,
                "ShippedDate": order.ShippedDate,
                "ShipPostalCode": order.ShipPostalCode,
                "ShipRegion": order.ShipRegion,
                "ShipVia": order.ShipVia,
            }
        )

    return jsonify(order_history)
