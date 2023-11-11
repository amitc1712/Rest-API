from flask import Blueprint
from controllers.product_controller import add_product, get_products, update_product

product_blueprint = Blueprint("product_blueprint", __name__)

# Get All Products
product_blueprint.route("/", methods=["GET"])(get_products)


# Create new Product
product_blueprint.route("/create", methods=["POST"])(add_product)


# Update a Product
product_blueprint.route("/update/<ProductID>", methods=["PUT"])(update_product)
