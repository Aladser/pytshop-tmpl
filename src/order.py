from src.product import Product
from src.log_mixin import LogMixin
from src.non_positive_prd_quantity_exception import NonPositiveProductQuantityException


class Order(LogMixin):
    __product: Product
    __quantity: int

    def __init__(self, product: Product, quantity: int):
        self.__product = product
        if quantity <= 0:
            raise NonPositiveProductQuantityException
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