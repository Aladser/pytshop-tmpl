from classes.product import Product


class Category:
    count = 0
    products_count = 0
    __products: list
    name: str
    description: str

    def __init__(self, name: str, products: list, description: str):
        """
        Категория
        :param name: имя
        :param products: товары
        :param description: описание
        """
        Category.count += 1
        Category.products_count += len(products)
        self.__products = products
        self.name = name
        self.description = description

    def add_product(self, new_product: Product):
        for i in range(0, len(self.__products)):
            if self.__products[i].name == new_product.name:
                self.__products[i].quantity += new_product.quantity
                if self.__products[i].price < new_product.price:
                    self.__products[i].price = new_product.price
                return
        self.__products.append(new_product)
        Category.products_count += 1

    @property
    def products(self):
        return [str(prd) for prd in self.__products]

    def __len__(self):
        prd_count = 0
        for prd in self.__products:
            prd_count += len(prd)
        return prd_count

    def __str__(self):
        return f"Название: {self.name}, количество продуктов: {self.len()} шт."