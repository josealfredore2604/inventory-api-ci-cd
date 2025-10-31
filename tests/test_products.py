import pytest
from src.app import app
from src.database import db
from src.models import Product

@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://dbuser:dbpass@localhost/test_inventory"
    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.session.remove()
        db.drop_all()

def test_create_product(client):
    response = client.post("/products/", json={"name": "Laptop", "price": 1200.99, "stock": 10})
    assert response.status_code == 201
    assert response.json["message"] == "Product created"

def test_get_products(client):
    client.post("/products/", json={"name": "Phone", "price": 699.99, "stock": 20})
    response = client.get("/products/")
    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]["name"] == "Phone"

def test_update_product(client):
    client.post("/products/", json={"name": "Tablet", "price": 500.00, "stock": 5})
    response = client.put("/products/1", json={"price": 550.00})
    assert response.status_code == 200
    assert response.json["message"] == "Product updated"

def test_delete_product(client):
    client.post("/products/", json={"name": "Monitor", "price": 200.00, "stock": 15})
    response = client.delete("/products/1")
    assert response.status_code == 200
    assert response.json["message"] == "Product deleted"
