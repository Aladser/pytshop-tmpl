from typing import Union


class IsNaturalNumber:
    @staticmethod
    def is_natural_number(value: Union[int, float]) -> bool:
        return value >= 0

    @staticmethod
    def verify_natural_number(value: Union[int, float]) -> bool:
        if value >= 0:
            return True
        else:
            raise ValueError('Число должно быть натуральным')