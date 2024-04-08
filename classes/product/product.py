class Product:
    __name: str
    __description: str
    __price: float
    __quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Товары
        :param name: имя
        :param price: цена
        :param quantity: количество
        :param description: описание
        """
        self.__name = name
        self.__description = description
        self.__price = price
        self.__quantity = quantity

    @classmethod
    def create(cls, prd_obj: dict):
        return cls(**prd_obj)

    @property
    def name(self) -> str:
        return self.__name

    @property
    def description(self) -> str:
        return self.__description

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, value: int):
        if value > 0:
            if value < self.__price:
                user_input = input('Вы действительно хотите снизить цену?')
                if user_input == 'y':
                    self.__price = value
            else:
                self.__price = value
        else:
            raise ValueError('Цена должна быть больше нуля')

    @property
    def quantity(self) -> int:
        return self.__quantity

    @quantity.setter
    def quantity(self, value: int):
        if value >= 0:
            self.__quantity = value
        else:
            raise ValueError('Количество не может быть отрицательным числом')

    def __add__(self, other) -> float:
        if isinstance(other, type(self)):
            return self.__price * self.__quantity + other.price * other.quantity
        else:
            raise TypeError('Объекты разных классов')

    def __str__(self) -> str:
        return f"{self.__name}, {self.__price} руб. Остаток: {self.__quantity} шт."

    def __len__(self) -> int:
        return self.__quantity
