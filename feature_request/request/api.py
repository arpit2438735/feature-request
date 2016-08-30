from flask import Blueprint, jsonify

from model import Request, Client, Product

request_api = Blueprint('request_api', __name__)


@request_api.route('/', methods=["GET"])
def get():
    requests = Request.query.all()

    feature_requests = []

    for feature_request in requests:
        feature_requests.append({'title': feature_request.title,
                                 'description': feature_request.description,
                                 'client_name': Client.find_by(id=feature_request.client).name,
                                 'client_priority': feature_request.client_priority,
                                 'target_date': feature_request.target_date,
                                 'product_area': Product.find_by(id=feature_request.product_area).name
                                 })

    return jsonify(feature_requests=feature_requests)