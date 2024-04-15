class NonPositiveProductQuantityException(Exception):
    """Исключение товара с неположительным количеством"""

    def __init__(self, product_name=None):
        if product_name:
            self.message = f"Товар {product_name} с неположительным количеством не может быть добавлен"
        else:
            self.message = 'Товар с неположительным количеством не может быть добавлен'

    def __str__(self):
        return self.message
