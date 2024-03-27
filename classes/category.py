class Category:
    """Категория"""
    count = 0
    products_count = 0
    title: str
    description: str
    # список продуктов класса classes.Product
    products: list

    def __init__(self, title: str, products: list, description: str):
        """Категория"""
        Category.count += 1
        Category.products_count += len(products)
        self.title = title
        self.products = products
        self.description = description