import pytest

from src import Order, NonPositiveProductQuantityException
from src.product import Product


@pytest.fixture
def params():
    return {
        'name': 'Хлеб',
        'price': 5,
        'quantity': 12,
        'description': 'Товар 1'
    }


@pytest.fixture
def params_str():
    return 'продукт: Хлеб, 5 руб. Остаток: 12 шт., количество: 3'


def test_init(params, params_str):
    order_count = 3
    product = Product(**params)
    order = Order(product, order_count)

    assert str(order) == params_str
    assert order.quantity == order_count
    assert order.price == params['price'] * order_count

    # обработка нулевого количества продукта
    print()
    for i in range(-1, 2):
        try:
            Order(product, i)
        except NonPositiveProductQuantityException as e:
            print(e)
        else:
            print('Товар добавлен')
        finally:
            print('Обработка добавления товара завершена.')
