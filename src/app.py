from flask import Flask
from models.category import db
from flask_migrate import Migrate
from routes.category_routes import category_blueprint
from routes.customer_routes import customer_blueprint
from routes.product_routes import product_blueprint
from routes.order_routes import order_blueprint


def create_app():
    app = Flask(__name__)
    app.config.from_object("config")

    db.init_app(app)

    return app


app = create_app()
app.register_blueprint(category_blueprint, url_prefix="/category")
app.register_blueprint(customer_blueprint, url_prefix="/customer")
app.register_blueprint(product_blueprint, url_prefix="/product")
app.register_blueprint(order_blueprint, url_prefix="/order")
migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run(debug=True)
