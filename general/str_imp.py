from abc import ABC, abstractmethod


class StrImpl(ABC):
    @abstractmethod
    def __str__(self):
        pass
