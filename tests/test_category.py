import pytest
from classes import Category, Product


@pytest.fixture
def title():
    return 'еда'


@pytest.fixture
def description():
    return 'здесь должна быть реклама'


@pytest.fixture
def products():
    return [
        Product(title='Хлеб', price=5, count=1, description='Товар 1')
    ]


@pytest.fixture
def category(title, products, description):
    return Category(title, products, description)


def test_init(category, title, products, description):
    print(category.products)
    assert category.title == title
    assert category.description == description
    assert Category.products_count == 1
    assert Category.count == 1
    # вывод продуктов
    assert category.products == ['Хлеб, 5 руб. Остаток: 1 шт.']
    # дубль товара
    prd4 = Product(title='Хлеб', price=5, count=1, description='Товар 1')
    category.add_product(prd4)
    assert  Category.products_count == 1
    # повышение цены
    prd4 = Product(title='Хлеб', price=10, count=1, description='Товар 1')
    category.add_product(prd4)
    assert  category.products[0].split(' ')[1] == '10'
    # понижение цены
    prd4 = Product(title='Хлеб', price=2, count=1, description='Товар 1')
    category.add_product(prd4)
    assert  category.products[0].split(' ')[1] == '10'
    # новый товар
    prd4 = Product(title='Сахар', price=20, count=4, description='Товар 3')
    category.add_product(prd4)
    assert  Category.products_count == 2
    prd4 = Product(title='Чай', price=15, count=3, description='Товар 2')
    category.add_product(prd4)
    assert  Category.products_count == 3