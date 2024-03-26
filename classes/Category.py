from classes import *


class Category:
    """Категория"""
    title: str
    """название"""
    # список продуктов класса classes.Product
    products: list
    """список продуктов"""
    description: str
    """описание"""
    count = 0
    """количество созданных категорий"""

    def __init__(self, title, products=[], description=""):
        """Категория"""
        Category.count += 1
        self.title = title
        self.products = products
        self.description = description

    def products_count(self):
        """ общее количество уникальных продуктов"""
        # пояснений дублей нет, так как дубли считаю ошибкой отправителя данных
        if len(self.products) == 0:
            return 0

        product_names_list = []
        for product in self.products:
            if product.title not in product_names_list:
                product_names_list.append(product.title)
        return len(product_names_list)

    def __repr__(self):
        return self.title
