from abc import ABC, abstractmethod


class BaseProduct(ABC):
    @classmethod
    @abstractmethod
    def create(cls, prd_obj: dict):
        pass
