class Product:
    __name: str
    __description: str
    __price: float
    __quantity: int

    def __init__(self, name: str, price: float, quantity: int, description: str):
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
            raise Exception('Цена должна быть больше нуля')

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value: int):
        self.__quantity = value

    def __repr__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."
