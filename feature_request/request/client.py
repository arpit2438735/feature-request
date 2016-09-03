from flask import Blueprint, jsonify
from model import Client

client = Blueprint('client', __name__)


@client.route('/', methods=['GET'])
def get():
    clients = Client.query.all()

    client_list = []

    for client in clients:
        client_list.append(client.to_json(client))

    return jsonify(clients=client_list)