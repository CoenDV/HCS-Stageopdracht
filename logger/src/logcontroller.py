from flask import Blueprint, request, jsonify
from src.logservice import LogService
import time

controller = Blueprint('controller', __name__)

@controller.route('/logs', methods=['GET'])
def get_all_logs():
    logs = LogService.get_all_logs()
    # return logs in JSON format and convert time to string
    return logs

@controller.route('/frontend_logs', methods=['POST'])
def save_frontend_log():
    log = request.get_json()
    LogService.save_frontend_log(log)
    return jsonify(log)

@controller.route('/backend_logs', methods=['POST'])
def save_backend_log():
    log = request.get_json()
    LogService.save_backend_log(log)
    return jsonify(log)

@controller.route('/llm_logs', methods=['POST'])
def save_llm_log():
    log = request.get_json()
    LogService.save_llm_log(log)
    return jsonify(log)
