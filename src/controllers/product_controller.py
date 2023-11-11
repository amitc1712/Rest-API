from flask import request, jsonify
from models.category import db
from models.product import ProductModel, product_schema, products_schema


# Create new product
def add_product():
    ProductID = request.json["ProductID"]
    CategoryID = request.json["CategoryID"]
    Discontinued = request.json["Discontinued"]
    ProductName = request.json["ProductName"]
    QuantityPerUnit = request.json["QuantityPerUnit"]
    ReorderLevel = request.json["ReorderLevel"]
    SupplierID = request.json["SupplierID"]
    UnitPrice = request.json["UnitPrice"]
    UnitsInStock = request.json["UnitsInStock"]
    UnitsOnOrder = request.json["UnitsOnOrder"]

    new_product = ProductModel(
        ProductID,
        CategoryID,
        Discontinued,
        ProductName,
        QuantityPerUnit,
        ReorderLevel,
        SupplierID,
        UnitPrice,
        UnitsInStock,
        UnitsOnOrder,
    )

    db.session.add(new_product)
    db.session.commit()

    return product_schema.jsonify(new_product)


# Get All Products
def get_products():
    all_products = ProductModel.query.all()
    result = products_schema.dump(all_products)
    return jsonify(result)


# Update a Product
def update_product(ProductID):
    product = ProductModel.query.get(ProductID)

    CategoryID = request.json["CategoryID"]
    Discontinued = request.json["Discontinued"]
    ProductName = request.json["ProductName"]
    QuantityPerUnit = request.json["QuantityPerUnit"]
    ReorderLevel = request.json["ReorderLevel"]
    SupplierID = request.json["SupplierID"]
    UnitPrice = request.json["UnitPrice"]
    UnitsInStock = request.json["UnitsInStock"]
    UnitsOnOrder = request.json["UnitsOnOrder"]

    product.CategoryID = CategoryID
    product.Discontinued = Discontinued
    product.ProductName = ProductName
    product.QuantityPerUnit = QuantityPerUnit
    product.ReorderLevel = ReorderLevel
    product.SupplierID = SupplierID
    product.UnitPrice = UnitPrice
    product.UnitsInStock = UnitsInStock
    product.UnitsOnOrder = UnitsOnOrder

    db.session.commit()

    return product_schema.jsonify(product)
