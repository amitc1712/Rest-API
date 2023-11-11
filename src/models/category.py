from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()


class CategoryModel(db.Model):
    __tablename__ = "categories"

    CategoryID = db.Column(db.Integer, primary_key=True)
    CategoryName = db.Column(db.String(20), unique=True)
    Description = db.Column(db.String(120))

    def __init__(self, CategoryID, CategoryName, Description):
        self.CategoryID = CategoryID
        self.CategoryName = CategoryName
        self.Description = Description


# Category Schema
class CategorySchema(ma.Schema):
    class Meta:
        fields = ("CategoryID", "CategoryName", "Description")


category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)
