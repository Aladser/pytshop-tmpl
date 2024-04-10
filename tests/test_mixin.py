from classes import Product, Grass, Category


def test_work():
    # product
    prd_params = {
        'name': 'Хлеб',
        'description': "товар",
        'price': 10,
        'quantity': 5
    }
    print()
    prd = Product(**prd_params)
    assert prd.name == prd_params['name']
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
    ctg = Category('еда', 'здесь должна быть реклама', [])