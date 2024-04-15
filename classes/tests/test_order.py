from classes import Order, NonPositiveProductQuantityException
from classes.product import Product


def test_init():
    product = Product(name='Хлеб', price=5, quantity=12, description='Товар 1')
    order = Order(product, 3)
    assert str(order) == 'продукт: Хлеб, 5 руб. Остаток: 12 шт., количество: 3'
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
