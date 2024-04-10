from classes.product.product import Product
from classes.mixin_log import MixinLog


class Category(MixinLog):
    quantity = 0
    products_quantity = 0
    __name: str
    __description: str
    __products: list

    def __init__(self, name: str, description: str, products: list):
        """
        Категория
        :param name: имя
        :param products: товары
        :param description: описание
        """
        Category.quantity += 1
        Category.products_quantity += len(products)
        self.__name = name
        self.__description = description
        self.__products = products
        super().__init__()

    @property
    def name(self) -> str:
        return self.__name

    @property
    def description(self) -> str:
        return self.__description

    def add_product(self, new_product):
        if not issubclass(type(new_product), Product):
            raise Exception(f"Объект {new_product} должен быть экземляром класс Product или его наследника")

        for i in range(0, len(self.__products)):
            if self.__products[i].name == new_product.name:
                self.__products[i].quantity += new_product.quantity
                if self.__products[i].price < new_product.price:
                    self.__products[i].price = new_product.price
                return
        self.__products.append(new_product)
        Category.products_quantity += 1

    @property
    def products(self) -> list:
        return [str(prd) for prd in self.__products]

    def __len__(self) -> int:
        prd_count = 0
        for prd in self.__products:
            prd_count += len(prd)
        return prd_count

    def __str__(self) -> str:
        return f"Название: {self.name}, количество продуктов: {self.__len__()} шт."
