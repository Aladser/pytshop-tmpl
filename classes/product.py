class Product:
    __price: float

    title: str
    description: str
    count: int

    def __init__(self, title: str, price: float, count: int, description: str = ""):
        self.__price = price
        self.title = title
        self.count = count
        self.description = description

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value > 0:
            if value < self.__price:
                user_input = input('Вы действительно хотите снизить цену?')
                if user_input == 'y':
                    self.__price = value
            else:
                self.__price = value
        else:
            raise Exception('Цена должна быть больше нуля')

    @price.deleter
    def price(self):
        self.__price = None

    @classmethod
    # в качестве примера берется экземпляр из Задания 2:
    # {название}, {цена} руб. Остаток: {количество} шт.
    def create(cls, product_str):
        title, params = product_str.split(',')
        params_list = params.split(' ')
        price = float(params_list[1])
        count = params_list[4]
        return cls(title, price, count)

    def __repr__(self):
        return f"{self.title}, {self.price} руб. Остаток: {self.count} шт."
