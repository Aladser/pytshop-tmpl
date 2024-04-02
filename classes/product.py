class Product:
    __name: str
    __description: str
    __price: float
    __quantity: int

    def __init__(self, name: str, price: float, quantity: int, description: str):
        """
        Товары
        :param name: имя
        :param price: цена
        :param quantity: количество
        :param description: описание
        """
        self.__price = price
        self.__name = name
        self.__quantity = quantity
        self.__description = description

    @classmethod
    def create(cls, prd_obj: dict):
        return cls(**prd_obj)

    @property
    def name(self):
        return self.__name

    @property
    def description(self):
        return self.__description

    @property
    def price(self):
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
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value: int):
        if value >= 0:
            self.__quantity = value
        else:
            raise ValueError('Количество не может быть отрицательным числом')

    def __add__(self, other):
        return self.price * self.quantity + other.price * other.quantity

    def __str__(self):
        return f"{self.__name}, {self.__price} руб. Остаток: {self.__quantity} шт."

    def __len__(self):
        return self.__quantity
