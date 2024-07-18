from flask import Blueprint, jsonify, request
from src.errors.error_controller import handle_errors
from src.main.factories.calculator_4_factory import calculator_4_factory

calc_route_bp = Blueprint("calc_routes", __name__)


@calc_route_bp.route("/calculators/4", methods=["POST"])
def calculator4():
    try:
        calc = calculator_4_factory()
        respose = calc.calculate(request)

        return jsonify(respose)

    except Exception as exception:
        error_response = handle_errors(exception)
        return jsonify(error_response["body"]), error_response["status_code"]
