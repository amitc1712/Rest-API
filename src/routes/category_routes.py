from flask import Blueprint
from controllers.category_controller import (
    add_category,
    get_categories,
    update_category,
)

blueprint = Blueprint("blueprint", __name__)

# Get All Categories
blueprint.route("/", methods=["GET"])(get_categories)


# Create new category
blueprint.route("/create", methods=["POST"])(add_category)


# Update a Category
blueprint.route("/update/<CategoryID>", methods=["PUT"])(update_category)
