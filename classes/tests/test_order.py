import pytest

from classes import Order
from classes.product import Product


def test_init():
    params = {'name':'Хлеб', 'price':5, 'quantity':12, 'description':'Товар 1'}
    product = Product(**params)
    params['quantity'] = -5
    with pytest.raises(ValueError):
        Product(**params)
    order = Order(product, 3)
    assert str(order) == 'продукт: Хлеб, 5 руб. Остаток: 12 шт., количество: 3'
