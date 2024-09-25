from typing import Dict, List

from .calculator_2 import Calculator2


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


class MockDriverHandler:
    def standard_derivation(self, number: List[float]) -> float:
        return 2  # um valor qualquer para testar a calculadora


def test_calculate():
    mock_request = MockRequest({"numbers": [2.12, 4.62, 1.32]})

    driver = MockDriverHandler()
    calculator_2 = Calculator2(driver)
    formated_response = calculator_2.calculate(mock_request)

    assert isinstance(formated_response,Dict)
    assert formated_response == {"data": {"Calculator": 2, "result": 0.5}}
