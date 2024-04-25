from abc import ABC, abstractmethod
from src.is_natural_number import IsNaturalNumber


class BaseProduct(ABC, IsNaturalNumber):
    @classmethod
    @abstractmethod
    def create(cls, prd_obj: dict):
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        pass

    @property
    @abstractmethod
    def price(self) -> float:
        pass

    @abstractmethod
    def __add__(self, other) -> float:
        pass
