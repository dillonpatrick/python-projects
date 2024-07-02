from typing import Dict, List
from flask import request as FlaskRequest


class Calculator2:
    def calculate(self, request: FlaskRequest) -> Dict:  # type: ignore
        body = request.json
        print(body)
        input_data = self._validate_body(body=body)
        print(input_data)

    def _validate_body(self, body: Dict) -> List:
        if "numbers" not in body:
            raise Exception("Body mal formatado")

        input_data = body["numbers"]
        return input_data
