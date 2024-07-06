from typing import Dict, List

from flask import request as FlaskRequest

from src.drivers.interfaces.driver_handler_interface import \
    DriverHandlerInterface


class Calculator2:
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler

    def calculate(self, request: FlaskRequest) -> Dict:  # type: ignore
        body = request.json
        input_data = self._validate_body(body=body)
        calculated_number = self._process_data(input_data)
        formated_response = self.__format_response(calculated_number)

        return formated_response

    def _validate_body(self, body: Dict) -> List:
        if "numbers" not in body:
            raise Exception("Body mal formatado")

        input_data = body["numbers"]
        return input_data

    def _process_data(self, input_data: List[float]) -> float:
        firs_process_result = [(num * 11) ** 0.95 for num in input_data]
        result = self.__driver_handler.standard_derivation(firs_process_result)
        return 1 / result

    def __format_response(self, calc_result: float) -> Dict:
        return {"data": {"Calculator": 2, "result": round(calc_result, 2)}}
