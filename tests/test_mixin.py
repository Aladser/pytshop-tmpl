from classes import Product, Grass, Category


def test_work():
    # product
    prd_params = {
        'name': 'Хлеб',
        'description': "товар",
        'price': 10,
        'quantity': 5
    }
    print('')
    prd = Product(**prd_params)
    prd.log()
    assert prd.name == prd_params['name']

    # наследник product
    grass_params = {
        'name': 'газонная',
        'description': 'городская',
        'price': 10,
        'quantity': 5,
        'country_manufacturer': 'Россия',
        'germination_period': '1 year',
        'color': 'зеленый'
    }
    print('----------')
    grass = Grass(**grass_params)
    grass.log()
    print('----------')
    ctg = Category('еда', 'здесь должна быть реклама', [prd, grass])
    ctg.log()