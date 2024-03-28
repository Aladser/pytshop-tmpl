from classes.product import Product


class Category:
    count = 0
    products_count = 0
    __products: list
    title: str
    description: str

    def __init__(self, title: str, products: list, description: str):
        Category.count += 1
        Category.products_count += len(products)
        self.__products = products
        self.title = title
        self.description = description

    def add_product(self, new_product: Product):
        # не вижу быстрее по скорости решения, чем перебор массива. В любом случае нужен перебор
        for i in range(0, len(self.__products)):
            if self.__products[i].title == new_product.title:
                self.__products[i].count += new_product.count
                if self.__products[i].price < new_product.price:
                    self.__products[i].price = new_product.price
                return
        self.__products.append(new_product)
        Category.products_count += 1

    @property
    def products(self):
        return [f"{prd.title}, {prd.price} руб. Остаток: {prd.count} шт." for prd in self.__products]
