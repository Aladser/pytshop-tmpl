import pytest
from src.product import Product, Grass, Smartphone


@pytest.fixture
def prd_params():
    return {
        'name': 'Хлеб',
        'description': "товар",
        'price': 10,
        'quantity': 5
    }


@pytest.fixture
def product(prd_params):
    return Product(**prd_params)


def test_init(prd_params):
    prd = Product.create(prd_params)
    prd_props_dict = prd.get_props_dict()
    for key in prd_props_dict:
        assert prd_props_dict[key] == prd_params[key]
    assert prd.description == prd_params['description']
    with pytest.raises(ValueError, match='Количество не может быть отрицательным числом'):
        prd.quantity = -5


def test_create(prd_params):
    prd = Product.create(prd_params)
    prd_props_dict = prd.get_props_dict()
    for key in prd_props_dict:
        assert prd_props_dict[key] == prd_params[key]


def test_price(monkeypatch, product):
    price = 15
    # установка новой цены
    product.price = price
    assert product.price == price
    # нулевая цена
    with pytest.raises(Exception):
        product.price = 0
    monkeypatch.setattr('builtins.input', lambda _: "y")
    product.price = 1


def test_add(product):
    grass_params = {
        'name': 'зеленая',
        'price': 10,
        'quantity': 5,
        'description': "товар 2",
        'country_manufacturer': 1,
        'germination_period': 2,
        'color': 'red'
    }
    smrt_params = {
        'name': 'Xiaomi',
        'price': 40000,
        'quantity': 3,
        'description': 'смартфон выполнен в корпусе серого цвета и предлагает мощные характеристики для комфортного решения разных задач',
        'perfomance': 687373,
        'model': '12X',
        'RAM': '32 Гб',
        'color': 'зеленый'
    }
    grass_1 = Grass(**grass_params)
    grass_2 = Grass(**grass_params)
    smartphone = Smartphone(**smrt_params)
    # один тип
    assert grass_1 + grass_2 == 100
    # разные типы
    with pytest.raises(TypeError):
        grass_1 + smartphone
    # родитель и наследник
    with pytest.raises(TypeError):
        product + grass_1
