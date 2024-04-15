# Шаблон интернет-магазина

+ *classes*
    * ``Category``
    * ``CategoryProductRange``
    * ``Order``
    * ``MixingLog`` - вывод информации о созданном объекте
    * ``NonPositiveProductQuantityException`` - исключение неположительного числа товаров
    * *product*
      + ``BaseProduct`` - абстрактный класс продукта
      + ``Product``
      + ``Grass``
      + ``Smartphone``
+ *load_data.py* - парсинг JSON файла и выгрузка категорий и товаров из него.
