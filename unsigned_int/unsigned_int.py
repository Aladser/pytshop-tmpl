class UnsignedInt:
    """беззнаковое целое"""
    __value: int

    def __init__(self, value: int):
        if self.check_unsigned_int_value(value):
            self.__value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_val: int):
        if self.check_unsigned_int_value(new_val):
            self.__value = new_val

    @staticmethod
    def check_unsigned_int_value(value) -> bool:
        if value >= 0:
            return True
        else:
            raise ValueError('Значение должно быть неотрицательным числом')

    def __add__(self, other: int):
        """сложение"""
        return self.__value + other

    def __sub__(self, other: int):
        """вычитание"""
        return self.__value - other

    def __mul__(self, other: int):
        """умножение"""
        return self.__value * other

    def __truediv__(self, other: int):
        """деление"""
        return self.__value // other

    def __floordiv__(self, other: int):
        """целочисленное деление"""
        return self.__value // other

    def __mod__(self, other: int):
        """остаток от деления"""
        return self.__value % other

    def __pow__(self, other: int):
        """возведение в степень"""
        return self.__value ** other

    def __str__(self):
        return str(self.__value)

    def __repr__(self):
        return str(self.__value)
