class Product:
    __price: float

    title: str
    description: str
    count: int

    def __init__(self, title: str, price: float, count: int, description: str):
        self.__price = price
        self.title = title
        self.count = count
        self.description = description

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
            print('Цена должна быть больше нуля')

    @price.deleter
    def price(self):
        self.__price = None

    @classmethod
    def create(cls, prd_obj: dict):
        return cls(
            prd_obj['title'],
            prd_obj['price'],
            prd_obj['count'],
            prd_obj['description']
        )

    def __repr__(self):
        return f"{self.title}, {self.price} руб. Остаток: {self.count} шт."
