class NullProductQuantityException(Exception):
    """Исключение товара с нулевым количеством"""
    def __init__(self):
        self.message = 'Товар с нулевым количеством не может быть добавлен'

    def __str__(self):
        return self.message
