from flask import Blueprint
from controllers.customer_controller import add_customer, get_customers, update_customer

customer_blueprint = Blueprint("customer_blueprint", __name__)

# Get All Customers
customer_blueprint.route("/", methods=["GET"])(get_customers)


# Create new customer
customer_blueprint.route("/create", methods=["POST"])(add_customer)


# Update a customer
customer_blueprint.route("/update/<CustomerID>", methods=["PUT"])(update_customer)
