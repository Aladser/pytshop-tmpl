class Category:
    """Категория"""
    title: str
    """название"""
    products: set
    """список продуктов"""
    description: str
    """описание"""
    count = 0
    """количество созданных категорий"""

    def __init__(self, title, products=[], description=""):
        """Категория"""
        self.title = title
        # логично, что категория должна иметь список уникальных продуктов
        self.products = set(products)
        self.description = description
        # логично, что категории тоже должны быть уникальны, но нельзя сделать мутабельный тип статическим?
        # по крайнем мере в других языках так
        Category.count += 1

    def products_count(self):
        """ общее количество уникальных продуктов"""
        return len(self.products)