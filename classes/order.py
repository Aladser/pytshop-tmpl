from classes.product import Product
from general import MixinLog, StrImpl


class Order(StrImpl, MixinLog):
    __product: Product
    __quantity: int

    def __init__(self, product: Product, quantity: int):
        self.__product = product
        self.__quantity = quantity
        super().__init__()

    @property
    def product(self):
        return self.__product

    @property
    def quantity(self):
        return self.__quantity

    @property
    def price(self):
        return self.__product.price * self.__quantity

    def __str__(self):
        return f"продукт: {self.product}, количество: {self.__quantity}"
