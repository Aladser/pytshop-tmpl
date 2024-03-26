class Product:
    """Товар"""
    title: str
    """название"""
    price: float
    """цена"""
    description: str
    """описание"""
    count: int
    """количество"""

    def __init__(self, title, price, count=0, description=""):
        """Товар"""
        self.title = title
        self.price = price
        self.count = count
        self.description = description
