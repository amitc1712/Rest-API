from flask import Blueprint
from controllers.category_controller import (
    add_category,
    get_categories,
    update_category,
)

category_blueprint = Blueprint("category_blueprint", __name__)

# Get All Categories
category_blueprint.route("/", methods=["GET"])(get_categories)


# Create new category
category_blueprint.route("/create", methods=["POST"])(add_category)


# Update a Category
category_blueprint.route("/update/<CategoryID>", methods=["PUT"])(update_category)
