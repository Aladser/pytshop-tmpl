import pytest
from src import Category, NonPositiveProductQuantityException, IsNaturalNumber
from src.product import Product, Grass


class TestCls:
    def __str__(self):
        return 'TestCls'


@pytest.fixture
def bread_params():
    return {
        'name': 'Хлеб',
        'price': 5,
        'quantity': 2,
        'description': 'Товар 1'
    }


@pytest.fixture
def bread(bread_params):
    return Product(**bread_params)


@pytest.fixture
def grass():
    grass_params = {
        'name': 'газонная',
        'description': 'городская',
        'price': 10,
        'quantity': 3,
        'country_manufacturer': 'Россия',
        'germination_period': '1 year',
        'color': 'зеленый'
    }
    return Grass(**grass_params)


@pytest.fixture
def milk():
    bread_params = {
        'name': 'Молоко',
        'price': 50,
        'quantity': 1,
        'description': 'с фермы'
    }
    return Product(**bread_params)


@pytest.fixture
def category_params(bread):
    return {
        'name': 'еда',
        'description': 'реклама еды',
        'products': [bread]
    }


def test_init(category_params, bread):
    category = Category(**category_params)
    assert category.name == category_params['name']
    assert category.description == category_params['description']
    assert category.products == [str(prd) for prd in category_params['products']]

    assert Category.quantity == 1
    assert Category.products_quantity == 1
    assert len(category) == 2
    assert category.products == [str(bread)]
    assert str(category) == f"Название: {category.name}, количество продуктов: {len(category)} шт."


def test_work(monkeypatch, category_params, bread, bread_params, grass, milk):
    category = Category(**category_params)

    # добавление товара
    category.add_product(grass)
    assert Category.products_quantity == 3
    category.add_product(milk)
    assert Category.products_quantity == 4

    # дубль товара
    category.add_product(bread)
    assert Category.products_quantity == 4

    # добавление не продукта или его потомка
    with pytest.raises(Exception, match='Объект TestCls должен быть экземляром класса Product или его наследника'):
        category.add_product(TestCls())

    # обновляется товар категории
    monkeypatch.setattr('builtins.input', lambda _: "y")
    bread_params['price'] = 10
    bread = Product(**bread_params)
    category.add_product(bread)
    assert Category.products_quantity == 4

    # нулевое количество товара
    bread_params['quantity'] = 0
    null_bread = Product(**bread_params)
    with pytest.raises(NonPositiveProductQuantityException):
        category.add_product(null_bread)
    with pytest.raises(NonPositiveProductQuantityException):
        Category('еда', 'здесь должна быть реклама', [bread, null_bread])

    # средняя цена
    category_params['products'] = []
    ctg = Category(**category_params)
    assert ctg.product_avg_price == 0
    bread_params['quantity'] = 1
    bread = Product(**bread_params)
    ctg.add_product(bread)
    assert ctg.product_avg_price == bread_params['price']

    # проверка IsNaturalNumber
    assert IsNaturalNumber.is_natural_number(5)
    with pytest.raises(ValueError, match='Число должно быть натуральным'):
        IsNaturalNumber.verify_natural_number(-5)
