from flask import Blueprint, request
import requests
from utils import load_file_config, HEADERS

vote_blueprints = Blueprint("vote_blueprints", __name__)
data_config = load_file_config()
url_base = data_config.get('url-backend-registry') + "/vote"


@vote_blueprints.route("/vote", methods=['GET'])
def get_all_votes() -> dict:
    url = url_base + "/all"
    response = requests.get(url, headers=HEADERS)
    return response.json()


@vote_blueprints.route("/vote/<string:id>", methods=['GET'])
def get_vote_by_id(id_: str) -> dict:
    url = url_base + f"/{id_}"
    response = requests.get(url, headers=HEADERS)
    return response.json()
