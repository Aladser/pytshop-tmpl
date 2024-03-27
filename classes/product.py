class Product:
    """Товар"""
    title: str
    price: float
    description: str
    count: int

    def __init__(self, title: str, price: float, count: int, description: str):
        """Товар"""
        self.title = title
        self.price = price
        self.count = count
        self.description = description

    def __repr__(self):
        return f"{self.title} {self.price} {self.count}"
