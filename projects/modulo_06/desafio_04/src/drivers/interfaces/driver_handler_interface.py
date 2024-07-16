from abc import ABC, abstractmethod
from typing import List


class DriverHandlerInterface(ABC):
    @abstractmethod
    def numbers_average(self, numbers: List[float]) -> float:
        pass
