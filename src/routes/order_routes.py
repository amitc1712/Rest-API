from flask import Blueprint
from controllers.order_controller import add_order, get_orders, update_order

order_blueprint = Blueprint("order_blueprint", __name__)

# Get All Orders
order_blueprint.route("/", methods=["GET"])(get_orders)


# Create new Order
order_blueprint.route("/create", methods=["POST"])(add_order)


# Update a Order
order_blueprint.route("/update/<OrderID>", methods=["PUT"])(update_order)
