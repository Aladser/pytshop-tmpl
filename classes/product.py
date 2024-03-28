class Product:
    __price: float

    title: str
    description: str
    count: int

    def __init__(self, title: str, price: float, count: int, description: str = ""):
        """Товар"""
        self.title = title
        self.price = price
        self.count = count
        self.description = description

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value > 0:
            self.__price = value
        else:
            raise Exception('Цена должна быть больше нуля')

    @classmethod
    # в качества примера берется экземпляр из Задания 2:
    # {название}, {цена} руб. Остаток: {количество} шт.
    def create(cls, product_str):
        title, params = product_str.split(',')
        params_list = params.split(' ')
        price = float(params_list[1])
        count = params_list[4]
        return cls(title, price, count)

    def __repr__(self):
        return f"{self.title}, {self.price} руб. Остаток: {self.count} шт."
