from flask import Blueprint, request
import requests
from utils import load_file_config, HEADERS

reports_blueprints = Blueprint("reports_blueprints", __name__)
data_config = load_file_config()
url_base = data_config.get('url-backend-registry') + "/reports"


@reports_blueprints.route("/reports", methods=['GET'])
def get_all_reports() -> dict:
    url = url_base + "/all"
    response = requests.get(url, headers=HEADERS)
    return response.json()


@reports_blueprints.route("/reports/<string:id>", methods=['GET'])
def get_reports_by_id(id_: str) -> dict:
    url = url_base + f"/{id_}"
    response = requests.get(url, headers=HEADERS)
    return response.json()


@reports_blueprints.route("/reports/insert", methods=['POST'])
def insert_reports() -> dict:
    reports = request.get_json()
    url = url_base + "/insert"
    response = requests.post(url, headers=HEADERS, json=reports)
    return response.json()


@reports_blueprints.route("/reports/update/<string:id_>", methods=['PUT'])
def update_reports(id_: str) -> dict:
    reports = request.get_json()
    url = url_base + "/update"
    response = requests.patch(url, headers=HEADERS, json=reports)
    return response.json()


@reports_blueprints.route("/reports/delete/<string:id_>", methods=['DELETE'])
def delete_reports(id_: str) -> dict:
    reports = request.get_json()
    url = url_base + "/delete"
    response = requests.delete(url, headers=HEADERS, json=reports)
    return response.json()

