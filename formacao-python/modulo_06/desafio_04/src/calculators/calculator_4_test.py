from typing import Dict, List

from .calculator_4 import Calculator4


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


class MockDriverHandler:
    def numbers_average(self, number: List[float]) -> float:
        return 5


def test_calculate():
    mock_request = MockRequest({"numbers": [1, 2, 3, 4, 5, 6, 7, 8, 9]})
    calculator_4 = Calculator4(MockDriverHandler())

    response = calculator_4.calculate(mock_request)

    assert response == {"data": {"Calculator": 4, "value": 5.0, "Success": True}}
