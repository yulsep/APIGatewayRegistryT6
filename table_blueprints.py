from flask import Blueprint, request
import requests
from utils import load_file_config, HEADERS

table_blueprints = Blueprint("table_blueprints", __name__)
data_config = load_file_config()
url_base = data_config.get('url-backend-registry') + "/table"


@table_blueprints.route("/table", methods=['GET'])
def get_all_tables() -> dict:
    url = url_base + "/all"
    response = requests.get(url, headers=HEADERS)
    return response.json()


@table_blueprints.route("/table/<string:id>", methods=['GET'])
def get_table_by_id(id_: str) -> dict:
    url = url_base + f"/{id_}"
    response = requests.get(url, headers=HEADERS)
    return response.json()
