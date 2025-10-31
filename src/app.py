from flask import Flask
import os
from .routes.products import products_bp
from .routes.sales import sales_bp
from .database import init_db

app = Flask(__name__)

# Configuración de la base de datos desde variables de entorno
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
    "DATABASE_URL", 
    "postgresql://dbuser:dbpass@localhost:5432/inventory"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Inicializar la base de datos
init_db(app)

# Registrar Blueprints
app.register_blueprint(products_bp, url_prefix="/products")
app.register_blueprint(sales_bp, url_prefix="/sales")

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

@app.route("/")
def init():
    return {"message": "Welcome to the API! :)"}, 200

if __name__ == "__main__":
    app.run(
        debug=os.getenv("FLASK_DEBUG", "False") == "True",
        host="0.0.0.0",
        port=5000
    )