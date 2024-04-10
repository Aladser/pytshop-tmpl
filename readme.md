# Шаблон интернет-магазина

+ ``classes``
    * ``product``
      + ``Product``
      + ``Grass``
      + ``Smartphone``
    * ``Category``
    * ``CategoryProductRange``
    * ``MixingCondoleLog`` - вывод информации о созданном объекте
+ ``tests``
    * ``product``
      + ``test_product``
      + ``test_grass``
      + ``test_smartphone``
    * ``test_category``
    * ``test_ctgprd_iterator``
    * ``test_mixing``
+ ``load_data.py`` - парсинг JSON файла и выгрузка категорий и товаров из него.
