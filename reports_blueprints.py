from flask import Blueprint, request
import requests
from utils import load_file_config, HEADERS

reports_blueprints = Blueprint("reports_blueprints", __name__)
data_config = load_file_config()
url_base = data_config.get('url-backend-registry') + "/reports"


# get reports by candidates
@reports_blueprints.route("/reports/votes_by_candidate", methods=['GET'])
def get_votes_by_candidate() -> dict:
    url = url_base + "/votes_by_candidate"
    response = requests.get(url, headers=HEADERS)
    return response.json()


@report_blueprints.route("/reports/votes_in_candidates/<string:id_candidate>", methods=['GET'])
def get_votes_in_candidates(id_candidate) -> dict:
    url = url_base + f"/votes_by_candidate/{id_candidate}"
    response = requests.get(url, headers=HEADERS)
    return response.json()


# get reports by tables.
@reports_blueprints.route("/reports/votes_by_tables", methods=['GET'])
def get_candidates_by_tables() -> dict:
    url = url_base + "/reports/votes_by_tables"
    response = requests.get(url, headers=HEADERS)
    return response.json()


@reports_blueprints.route("/reports/votes_in_table/<string:table_id>", methods=['GET'])
def get_candidates_by_tables(table_id) -> dict:
    url = url_base + f"/reports/votes_in_table/{table_id}"
    response = requests.get(url, headers=HEADERS)
    return response.json()


# get reports by political parts
@reports_blueprints.route("/reports/votes_by_political_party", methods=['GET'])
def get_votes_by_political_party() -> dict:
    url = url_base + "/reports/votes_by_political_party"
    response = requests.get(url, headers=HEADERS)
    return response.json()


@reports_blueprints.route("/reports/percentage_votes_parties", methods=['GET'])
def get_percentage_votes_parties() -> dict:
    url = url_base + "/reports/percentage_votes_parties"
    response = requests.get(url, headers=HEADERS)
    return response.json()


