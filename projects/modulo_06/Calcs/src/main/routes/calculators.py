from flask import Blueprint, jsonify, request

from src.main.factories.calculator1_factory import calculator1_factory
from src.main.factories.calculator2_factory import calculator2_factory
from src.main.factories.calculator3_factory import calculator3_factory

calc_route_bp = Blueprint("calc_routes", __name__)


@calc_route_bp.route("/calculators/1", methods=["POST"])
def calculator1():
    calc = calculator1_factory()
    response = calc.calculate(request)

    return jsonify(response), 200


@calc_route_bp.route("/calculators/2", methods=["POST"])
def calculator2():
    calc = calculator2_factory()
    response = calc.calculate(request)

    return jsonify(response), 200


@calc_route_bp.route("/calculators/3", methods=["POST"])
def calculator3():
    calc = calculator3_factory()
    response = calc.calculate(request)

    return jsonify(response), 200
