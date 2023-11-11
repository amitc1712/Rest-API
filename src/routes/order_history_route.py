from flask import Blueprint
from controllers.orderhistory_controller import get_order_history

order_history_blueprint = Blueprint("order_history_blueprint", __name__)

# Order history of a given customer
order_history_blueprint.route("/<CustomerID>", methods=["GET"])(get_order_history)
