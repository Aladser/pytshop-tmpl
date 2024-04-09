from abc import ABC, abstractmethod


class BaseProduct(ABC):
    @abstractmethod
    def create(cls, prd_obj: dict):
        pass
