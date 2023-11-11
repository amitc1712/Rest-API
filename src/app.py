from flask import Flask
from models.category import db
from flask_migrate import Migrate
from routes.category_routes import blueprint

app = Flask(__name__)

app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "mysql+pymysql://root:1234@localhost:3306/northwind"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


def create_app():
    app = Flask(__name__)
    app.config.from_object("config")

    db.init_app(app)

    return app


app = create_app()
app.register_blueprint(blueprint, url_prefix="/category")
migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run(debug=True)
