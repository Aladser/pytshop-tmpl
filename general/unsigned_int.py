class UnsignedInt:
    __value: int

    def __init__(self, value):
        if self.check_unsigned_int_value(value):
            self.__value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_val):
        if self.check_unsigned_int_value(new_val):
            self.__value = new_val

    @staticmethod
    def check_unsigned_int_value(value) -> bool:
        if value >= 0:
            return True
        else:
            raise Exception('Значение должно быть неотрицательным числом')

    def __add__(self, other):
        """сложение"""
        if self.check_unsigned_int_value(other):
            return self.__value + other

    def __sub__(self, other):
        """вычитание"""
        if self.check_unsigned_int_value(other):
            rslt = self.__value - other
            return rslt if rslt >= 0 else 0

    def __mul__(self, other):
        """умножение"""
        if self.check_unsigned_int_value(other):
            return self.__value * other

    def __truediv__(self, other):
        """деление"""
        if self.check_unsigned_int_value(other):
            return self.__value / other

    def __floordiv__(self, other):
        """целочисленное деление"""
        if self.check_unsigned_int_value(other):
            return self.__value // other

    def __mod__(self, other):
        """остаток от деления"""
        if self.check_unsigned_int_value(other):
            return self.__value % other

    def __pow__(self, other):
        """возведение в степень"""
        if self.check_unsigned_int_value(other):
            return self.__value ** other

    def __str__(self):
        return str(self.__value)

    def __repr__(self):
        return str(self.__value)
