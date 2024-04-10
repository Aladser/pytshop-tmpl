from classes import Product


class Order:
    __product: Product
    __quantity: int

    def __init__(self, product: Product, quantity: int):
        self.__product = product
        self.__quantity = quantity

    @property
    def product(self):
        return self.__product

    @property
    def quantity(self):
        return self.__quantity

    @property
    def price(self):
        return self.__product.price * self.__quantity
