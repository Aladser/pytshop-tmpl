class Category:
    """Категория"""
    count = 0
    title: str
    description: str
    # список продуктов класса classes.Product
    products: list
    products_count: int

    def __init__(self, title: str, products: list, description: str):
        """Категория"""
        Category.count += 1
        self.title = title
        self.products = products
        self.products_count = len(self.products)
        self.description = description

    def __repr__(self):
        return self.title
