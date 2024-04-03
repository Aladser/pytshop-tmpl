import pytest
from classes import Category, Product


@pytest.fixture
def products():
    return [
        Product(name='Хлеб', price=5, quantity=12, description='Товар 1')
    ]


@pytest.fixture
def category(products):
    return Category('еда', products, 'здесь должна быть реклама')


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
    prd = Product(name='Хлеб', price=5, quantity=1, description='Товар 1')
    category.add_product(prd)
    assert Category.products_quantity == 2
    # дубль товара
    prd = Product(name='Хлеб1', price=5, quantity=1, description='Товар 1')
    category.add_product(prd)
    assert Category.products_quantity == 3
