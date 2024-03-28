
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

    def add_product(self, prd):
        self.__products.append(prd)

    @property
    def products(self):
        return [f"{prd.title}, {prd.price} руб. Остаток: {prd.count} шт." for prd in self.__products]