from typing import List

import numpy as np

from .interfaces.driver_handler_interface import DriverHandlerInterface


class NumpyHandler(DriverHandlerInterface):
    def __init__(self) -> None:
        self.__np = np

    def numbers_average(self, numbers: List[float]) -> float:
        return self.__np.average(numbers)
