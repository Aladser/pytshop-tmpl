from src import Category
from src.product import Product, Grass


def test_work():
    # tests
    prd_params = {
        'name': 'Хлеб',
        'description': "товар",
        'price': 10,
        'quantity': 5
    }
    print()
    prd = Product(**prd_params)
    prd.log()
    assert prd.name == prd_params['name']

    # grass
    params = {
        'name': 'газонная',
        'description': 'городская',
        'price': 10,
        'quantity': 5,
        'country_manufacturer': 'Россия',
        'germination_period': '1 year',
        'color': 'зеленый'
    }
    grass = Grass(**params)
    grass.log()

    # category
    ctg = Category('еда', 'здесь должна быть реклама', [prd, grass])
    ctg.log()

    # get_props_dict()
    props_dict = ctg.get_props_dict()
    print(props_dict)
