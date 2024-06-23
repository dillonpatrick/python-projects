from flask import Blueprint, jsonify, request

calc_route_bp = Blueprint("calc_routes", __name__)


@calc_route_bp.route("/calculators/1", methods=["POST"])
def calculator():
    print(request.json)
    return jsonify({"success": True}), 200
