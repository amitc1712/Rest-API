from models.category import db, ma


class CustomerModel(db.Model):
    __tablename__ = "customers"

    CustomerID = db.Column(db.Integer, primary_key=True)
    CompanyName = db.Column(db.String(120), unique=True, nullable=False)
    ContactName = db.Column(db.String(120), nullable=False)
    ContactTitle = db.Column(db.String(120), nullable=False)
    Address = db.Column(db.String(20), nullable=True)
    City = db.Column(db.String(20), nullable=True)
    Region = db.Column(db.String(120), nullable=False)
    PostalCode = db.Column(db.String(120), nullable=False)
    Country = db.Column(db.String(120), nullable=False)
    Phone = db.Column(db.String(120), nullable=False)
    Fax = db.Column(db.String(120), nullable=False)

    def __init__(
        self,
        CustomerID,
        CompanyName,
        ContactName,
        ContactTitle,
        Address,
        City,
        Region,
        PostalCode,
        Country,
        Phone,
        Fax,
    ):
        self.CustomerID = CustomerID
        self.CompanyName = CompanyName
        self.ContactName = ContactName
        self.ContactTitle = ContactTitle
        self.Address = Address
        self.City = City
        self.Region = Region
        self.PostalCode = PostalCode
        self.Country = Country
        self.Phone = Phone
        self.Fax = Fax


# Customer Schema
class CustomerSchema(ma.Schema):
    class Meta:
        fields = (
            "CustomerID",
            "CompanyName",
            "ContactName",
            "ContactTitle",
            "Address",
            "City",
            "Region",
            "PostalCode",
            "Country",
            "Phone",
            "Fax",
        )


customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)
