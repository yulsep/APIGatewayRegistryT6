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
