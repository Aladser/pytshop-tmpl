class NonPositiveProductQuantityException(Exception):
    """Исключение товара с неположительным количеством"""

    def __init__(self, product_name=None):
        product_name_str = f"Товар {product_name}" if product_name else 'Товар'
        self.message = f"{product_name_str} с неположительным количеством не может быть добавлен"

    def __str__(self):
        return self.message
