from classes import Order
from classes.product import Product


def test_init():
    print()
    product = Product(name='Хлеб', price=5, quantity=12, description='Товар 1')
    order = Order(product, 3)
    assert str(order) == 'продукт: Хлеб, 5 руб. Остаток: 12 шт., количество: 3'
