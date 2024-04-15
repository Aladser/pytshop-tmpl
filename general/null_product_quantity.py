class NullProductQuantity(Exception):
    """Исключение товара с нулевым количеством"""
    def __init__(self, *args):
        self.message = args[0] if args else 'Товар с нулевым количеством'

    def __str__(self):
        return self.message
