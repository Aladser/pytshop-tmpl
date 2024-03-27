import json
from classes import Category, Product

products_file = 'data/products.json'
if __name__ == '__main__':
    with open(products_file) as file:
        data = json.load(file)

    categories = []
    # парсинг JSON-файла с созданием категорий и их продуктов
    for item in data:
        products_list = []
        for prd in item['products']:
            product = Product(prd['name'],prd['price'],prd['quantity'],prd['description'] )
            products_list.append(product)
        category = Category(item['name'], products_list, item['description'])
        categories.append(category)

    # вывод полученных данных
    for ctg in categories:
        print(f"Название: {ctg.title}")
        print(f"Описание: {ctg.description}")
        print(f"Товары (количество:{ctg.products_count}):")
        [print(prd) for prd in ctg.products]
        print('-----')