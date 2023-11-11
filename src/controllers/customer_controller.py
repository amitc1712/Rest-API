from flask import request, jsonify
from models.category import db
from models.customer import CustomerModel, customer_schema, customers_schema


# Create new customer
def add_customer():
    CustomerID = request.json["CustomerID"]
    CompanyName = request.json["CompanyName"]
    ContactName = request.json["ContactName"]
    ContactTitle = request.json["ContactTitle"]
    Address = request.json["Address"]
    City = request.json["City"]
    Region = request.json["Region"]
    PostalCode = request.json["PostalCode"]
    Country = request.json["Country"]
    Phone = request.json["Phone"]
    Fax = request.json["Fax"]

    new_customer = CustomerModel(
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
    )

    db.session.add(new_customer)
    db.session.commit()

    return customer_schema.jsonify(new_customer)


# Get All Customers
def get_customers():
    all_customers = CustomerModel.query.all()
    result = customers_schema.dump(all_customers)
    return jsonify(result)


# Update a Customer
def update_customer(CustomerID):
    customer = CustomerModel.query.get(CustomerID)

    CompanyName = request.json["CompanyName"]
    ContactName = request.json["ContactName"]
    ContactTitle = request.json["ContactTitle"]
    Address = request.json["Address"]
    City = request.json["City"]
    Region = request.json["Region"]
    PostalCode = request.json["PostalCode"]
    Country = request.json["Country"]
    Phone = request.json["Phone"]
    Fax = request.json["Fax"]

    customer.CompanyName = CompanyName
    customer.ContactName = ContactName
    customer.ContactTitle = ContactTitle
    customer.Address = Address
    customer.City = City
    customer.Region = Region
    customer.PostalCode = PostalCode
    customer.Country = Country
    customer.Phone = Phone
    customer.Fax = Fax

    db.session.commit()

    return customer_schema.jsonify(customer)
