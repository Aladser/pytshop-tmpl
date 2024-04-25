from typing import Union


class IsNaturalNumber:
    @staticmethod
    def is_natural_number(value: Union[int, float]) -> bool:
        '''проверяет является ли число value натуральным'''
        return value >= 0

    @staticmethod
    def verify_natural_number(value: Union[int, float]):
        '''проверяет является ли число value натуральным возвращает исключение, если ложно'''
        if value < 0:
            raise ValueError('Число должно быть натуральным')
