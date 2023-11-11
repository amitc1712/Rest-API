from flask import request, jsonify
from models.category import db, CategoryModel, category_schema, categories_schema


# Create new category
def add_category():
    CategoryID = request.json["CategoryID"]
    CategoryName = request.json["CategoryName"]
    Description = request.json["Description"]

    new_category = CategoryModel(CategoryID, CategoryName, Description)

    db.session.add(new_category)
    db.session.commit()

    return category_schema.jsonify(new_category)


# Get All Categories
def get_categories():
    all_categories = CategoryModel.query.all()
    result = categories_schema.dump(all_categories)
    return jsonify(result)


# Update a Category
def update_category(CategoryID):
    category = CategoryModel.query.get(CategoryID)

    CategoryName = request.json["CategoryName"]
    Description = request.json["Description"]

    category.CategoryName = CategoryName
    category.Description = Description

    db.session.commit()

    return category_schema.jsonify(category)
