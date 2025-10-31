import pytest
from src.app import app
from src.database import db
from src.models import Product, Sale

@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://dbuser:dbpass@localhost/test_inventory"
    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.session.remove()
        db.drop_all()

def test_register_sale(client):
    client.post("/products/", json={"name": "Keyboard", "price": 50.00, "stock": 30})
    response = client.post("/sales/", json={"product_id": 1, "quantity": 5})
    assert response.status_code == 201
    assert response.json["message"] == "Sale registered"

def test_get_sales(client):
    client.post("/products/", json={"name": "Mouse", "price": 20.00, "stock": 25})
    client.post("/sales/", json={"product_id": 1, "quantity": 3})
    response = client.get("/sales/")
    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]["quantity"] == 3

def test_register_sale_insufficient_stock(client):
    client.post("/products/", json={"name": "Printer", "price": 150.00, "stock": 2})
    response = client.post("/sales/", json={"product_id": 1, "quantity": 5})
    assert response.status_code == 400
    assert response.json["error"] == "Not enough stock"
