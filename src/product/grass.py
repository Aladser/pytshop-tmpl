from src.product.product import Product


# не вижу смысла создавать класс газонная трава. Максимум можно создать наследника класса Трава
class Grass(Product):
    country_manufacturer: str
    germination_period: int
    color: str

    def __init__(self,
                 name: str, description: str, price: float, quantity: int,
                 country_manufacturer: str, germination_period: int, color: str
                 ):
        """
        Трава
        :param name: имя
        :param description: описание
        :param price: цена
        :param quantity: количество
        :param country_manufacturer: страна-производитель
        :param germination_period: срок прорастания
        :param color: цвет
        """
        super().__init__(name, description, price, quantity)
        self.country_manufacturer = country_manufacturer
        self.germination_period = germination_period
        self.color = color
