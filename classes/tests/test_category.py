import pytest
from classes import Category, NonPositiveProductQuantityException
from classes.product import Product, Grass


class TestCls:
    pass


@pytest.fixture()
def prd_params():
    return {
        'name': 'Хлеб',
        'price': 5,
        'quantity': 12,
        'description': 'Товар'
    }


@pytest.fixture
def ctg_params(prd_params):
    return {
        'name': 'еда',
        'description': 'здесь должна быть реклама',
        'products': [Product(**prd_params)]
    }


@pytest.fixture
def category(ctg_params):
    return Category(**ctg_params)


def test_init(ctg_params):
    category = Category(**ctg_params)
    assert category.name == ctg_params['name']
    assert category.description == ctg_params['description']
    assert category.products == [str(prd) for prd in ctg_params['products']]

    assert Category.products_quantity == 1
    assert Category.quantity == 1

    assert len(category) == 12


def test_work(category):
    bread_params = {
        'name': 'Хлеб',
        'description': 'пекарня',
        'price': 5,
        'quantity': 1,
    }
    grass_params = {
        'name': 'газонная',
        'description': 'городская',
        'price': 10,
        'quantity': 1,
        'country_manufacturer': 'Россия',
        'germination_period': '1 year',
        'color': 'зеленый'
    }
    bread = Product(**bread_params)
    grass = Grass(**grass_params)

    # добавление товара
    category.add_product(bread)
    assert Category.products_quantity == 2
    category.add_product(grass)
    assert Category.products_quantity == 3

    # добавление непродукта
    with pytest.raises(Exception):
        category.add_product(TestCls())

    # дубль товара
    category.add_product(bread)
    assert Category.products_quantity == 3

    # нулевое количество товара
    bread_params['name'] = 'Хлеб 2'
    bread_params['quantity'] = 0
    null_bread = Product(**bread_params)
    match_str = f"Товар {bread_params['name']} с неположительным количеством не может быть добавлен"

    with pytest.raises(NonPositiveProductQuantityException, match=match_str):
        Category('еда', 'здесь должна быть реклама', [bread, null_bread])
    with pytest.raises(NonPositiveProductQuantityException, match=match_str):
        category.add_product(null_bread)

    # средняя цена
    ctg = Category('еда', 'здесь должна быть реклама', [])
    assert ctg.product_avg_price == 0
    ctg.add_product(bread)
    assert ctg.product_avg_price == 5
