from flask import Blueprint, request
import requests
from utils import load_file_config, HEADERS

political_party_blueprints = Blueprint("political_party_blueprints", __name__)
data_config = load_file_config()
url_base = data_config.get('url-backend-registry') + "/political_party"


@political_party_blueprints.route("/political_party", methods=['GET'])
def get_all_parties() -> dict:
    url = url_base + "/all"
    response = requests.get(url, headers=HEADERS)
    return response.json()


@political_party_blueprints.route("/political_party/<string:id>", methods=['GET'])
def get_parties_by_id(id_: str) -> dict:
    url = url_base + f"/{id_}"
    response = requests.get(url, headers=HEADERS)
    return response.json()


@political_party_blueprints.route("/political_party/insert", methods=['POST'])
def insert_political_party() -> dict:
    political_party = request.get_json()
    url = url_base + "/insert"
    response = requests.post(url, headers=HEADERS, json=political_party)
    return response.json()


@political_party_blueprints.route("/political_party/update/<string:id_>", methods=['PUT'])
def update_political_party(id_: str) -> dict:
    political_party = request.get_json()
    url = url_base + "/update"
    response = requests.patch(url, headers=HEADERS, json=political_party)
    return response.json()


@political_party_blueprints.route("/political_party/delete/<string:id_>", methods=['DELETE'])
def delete_political_party(id_: str) -> dict:
    political_party = request.get_json()
    url = url_base + "/delete"
    response = requests.delete(url, headers=HEADERS, json=political_party)
    return response.json()

