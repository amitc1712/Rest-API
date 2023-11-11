from models.category import db, ma


class OrderModel(db.Model):
    __tablename__ = "orders"

    OrderID = db.Column(db.Integer, primary_key=True)
    CustomerID = db.Column(db.String(20))
    EmployeeID = db.Column(db.Integer)
    Freight = db.Column(db.Double)
    OrderDate = db.Column(db.String(20))
    RequiredDate = db.Column(db.String(20))
    ShipAddress = db.Column(db.String(20))
    ShipCity = db.Column(db.String(20))
    ShipCountry = db.Column(db.String(20))
    ShipName = db.Column(db.String(20))
    ShippedDate = db.Column(db.String(20))
    ShipPostalCode = db.Column(db.String(20))
    ShipRegion = db.Column(db.String(20))
    ShipVia = db.Column(db.Integer)

    def __init__(
        self,
        OrderID,
        CustomerID,
        EmployeeID,
        Freight,
        OrderDate,
        RequiredDate,
        ShipAddress,
        ShipCity,
        ShipCountry,
        ShipName,
        ShippedDate,
        ShipPostalCode,
        ShipRegion,
        ShipVia,
    ):
        self.OrderID = OrderID
        self.CustomerID = CustomerID
        self.EmployeeID = EmployeeID
        self.Freight = Freight
        self.OrderDate = OrderDate
        self.RequiredDate = RequiredDate
        self.ShipAddress = ShipAddress
        self.ShipCity = ShipCity
        self.ShipCountry = ShipCountry
        self.ShipName = ShipName
        self.ShippedDate = ShippedDate
        self.ShipPostalCode = ShipPostalCode
        self.ShipRegion = ShipRegion
        self.ShipVia = ShipVia


# Order Schema
class OrderSchema(ma.Schema):
    class Meta:
        fields = (
            "OrderID",
            "CustomerID",
            "EmployeeID",
            "Freight",
            "OrderDate",
            "RequiredDate",
            "ShipAddress",
            "ShipCity",
            "ShipCountry",
            "ShipName",
            "ShippedDate",
            "ShipPostalCode",
            "ShipRegion",
            "ShipVia",
        )


order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)
