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

    def __init__(self, title, price, description="", count=0):
        """Товар"""
        self.title = title
        self.price = price
        self.description = description
        self.count = count
