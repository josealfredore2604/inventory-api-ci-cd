from flask import Blueprint, request, jsonify
from src.models import Product
from src.database import db

products_bp = Blueprint("products", __name__)

@products_bp.route("/", methods=["POST"])
def create_product():
    data = request.json
    product = Product(name=data["name"], price=data["price"], stock=data["stock"])
    db.session.add(product)
    db.session.commit()
    return jsonify({"message": "Product created", "id": product.id}), 201

@products_bp.route("/", methods=["GET"])
def get_products():
    products = Product.query.all()
    return jsonify([{"id": p.id, "name": p.name, "price": p.price, "stock": p.stock} for p in products])

@products_bp.route("/<int:id>", methods=["PUT"])
def update_product(id):
    data = request.json
    product = Product.query.get_or_404(id)
    product.name = data.get("name", product.name)
    product.price = data.get("price", product.price)
    product.stock = data.get("stock", product.stock)
    db.session.commit()
    return jsonify({"message": "Product updated"})

@products_bp.route("/<int:id>", methods=["DELETE"])
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({"message": "Product deleted"})
