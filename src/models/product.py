from models.category import db, ma


class ProductModel(db.Model):
    __tablename__ = "products"

    ProductID = db.Column(db.Integer, primary_key=True)
    CategoryID = db.Column(db.Integer)
    Discontinued = db.Column(db.Integer)
    ProductName = db.Column(db.String(20))
    QuantityPerUnit = db.Column(db.String(20))
    ReorderLevel = db.Column(db.Integer)
    SupplierID = db.Column(db.Integer)
    UnitPrice = db.Column(db.Double)
    UnitsInStock = db.Column(db.Integer)
    UnitsOnOrder = db.Column(db.Integer)

    def __init__(
        self,
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
    ):
        self.ProductID = ProductID
        self.CategoryID = CategoryID
        self.Discontinued = Discontinued
        self.ProductName = ProductName
        self.QuantityPerUnit = QuantityPerUnit
        self.ReorderLevel = ReorderLevel
        self.SupplierID = SupplierID
        self.UnitPrice = UnitPrice
        self.UnitsInStock = UnitsInStock
        self.UnitsOnOrder = UnitsOnOrder


# Product Schema
class ProductSchema(ma.Schema):
    class Meta:
        fields = (
            "ProductID",
            "CategoryID",
            "Discontinued",
            "ProductName",
            "QuantityPerUnit",
            "ReorderLevel",
            "SupplierID",
            "UnitPrice",
            "UnitsInStock",
            "UnitsOnOrder",
        )


product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
