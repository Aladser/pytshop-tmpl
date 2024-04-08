import pytest
from classes import Category, Product


class TestCls:
    pass


@pytest.fixture
def products():
    return [
        Product(name='Хлеб', price=5, quantity=12, description='Товар 1')
    ]


@pytest.fixture
def category(products):
    return Category('еда', 'здесь должна быть реклама', products)


def test_init(category, products):
    assert category.name == 'еда'
    assert category.description == 'здесь должна быть реклама'
    assert category.products == [str(prd) for prd in products]
    assert Category.products_quantity == 1
    assert Category.quantity == 1
    assert len(category) == 12
    assert category.products == ['Хлеб, 5 руб. Остаток: 12 шт.']


def test_work(category):
    # добавление товара
    category.add_product(Product(name='Хлеб', price=5, quantity=1, description='Товар 1'))
    assert Category.products_quantity == 2
    with pytest.raises(Exception):
        category.add_product(TestCls())
    # дубль товара
    prd = Product(name='Хлеб1', price=5, quantity=1, description='Товар 1')
    category.add_product(prd)
    assert Category.products_quantity == 3
