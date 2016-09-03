from flask import Blueprint, jsonify
from model import Product

product = Blueprint('product', __name__)


@product.route('/', methods=['GET'])
def get():
    products = Product.query.all()

    product_list = []

    for product in products:
        product_list.append(product.to_json(product))

    return jsonify(products=product_list)