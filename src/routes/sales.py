from flask import Blueprint, request, jsonify
from src.models import Sale, Product
from src.database import db

sales_bp = Blueprint("sales", __name__)

@sales_bp.route("/", methods=["POST"])
def register_sale():
    data = request.json
    product = Product.query.get_or_404(data["product_id"])
    if product.stock < data["quantity"]:
        return jsonify({"error": "Not enough stock"}), 400
    sale = Sale(
        product_id=product.id,
        quantity=data["quantity"],
        total_price=product.price * data["quantity"]
    )
    product.stock -= data["quantity"]
    db.session.add(sale)
    db.session.commit()
    return jsonify({"message": "Sale registered", "id": sale.id}), 201

@sales_bp.route("/", methods=["GET"])
def get_sales():
    sales = Sale.query.all()
    return jsonify([{
        "id": s.id,
        "product_id": s.product_id,
        "quantity": s.quantity,
        "total_price": s.total_price
    } for s in sales])
