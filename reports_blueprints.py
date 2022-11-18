from flask import Blueprint, request
import requests
from utils import load_file_config, HEADERS

reports_blueprints = Blueprint("reports_blueprints", __name__)
data_config = load_file_config()
url_base = data_config.get('url-backend-registry') + "/reports"


@reports_blueprints.route("/reports/votes_by_candidate", methods=['GET'])
def get_votes_by_candidate() -> dict:
    url = url_base + "/votes_by_candidate"
    response = requests.get(url, headers=HEADERS)
    return response.json()


@reports_blueprints.route("/reports/candidates_by_tables", methods=['GET'])
def get_candidates_by_tables() -> dict:
    url = url_base + "/candidates_by_tables"
    response = requests.get(url, headers=HEADERS)
    return response.json()


@reports_blueprints.route("/reports/votes_by_political_party", methods=['GET'])
def get_votes_by_political_party() -> dict:
    url = url_base + "/votes_by_political_party"
    response = requests.get(url, headers=HEADERS)
    return response.json()


@reports_blueprints.route("/reports/percentage_votes_parties", methods=['GET'])
def get_percentage_votes_parties() -> dict:
    url = url_base + "/percentage_votes_parties"
    response = requests.get(url, headers=HEADERS)
    return response.json()

