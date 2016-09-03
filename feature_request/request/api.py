from flask import Blueprint, jsonify, request
import json

from model import Request

request_api = Blueprint('request_api', __name__)


@request_api.route('/', methods=["GET"])
def get():
    requests = Request.query.all()

    feature_requests = []

    for feature_request in requests:
        feature_requests.append(feature_request.to_json(feature_request))

    return jsonify(feature_requests=feature_requests)


@request_api.route('/', methods=['POST'])
def post():
    feature_request_response = json.loads(request.data)
    feature_request = Request(feature_request_response['title'], feature_request_response['description'],
                              feature_request_response['client_id'], feature_request_response['client_priority'],
                              feature_request_response['target_date'], feature_request_response['product_id'])

    feature_request.insert(feature_request)

    return jsonify({
            'status': 'success',
            'reason': 'Feature request added',
            'feature_request': feature_request.to_json(feature_request)
        }), 201


@request_api.route('/<feature_request_id>', methods=['PUT'])
def put(feature_request_id):

    feature_request = Request.find_by(id=feature_request_id)

    if feature_request is None:
        return jsonify({'status': 'fail',
                        'reason': 'Resource not found'}), 404

    feature_request_response = json.loads(request.data)
    feature_request = feature_request.update_request(feature_request, feature_request_response)
    feature_request.save()

    return jsonify({
        'status': 'success',
        'reason': 'Feature request updated',
        'feature_request': feature_request.to_json(feature_request)
    })