# Решение

## С Pyspark я не знаком, поэтому решение здесь не моё. Я лишь нашел его и проверил, что оно рабочее.
Ссылка на репозиторий автора - https://github.com/Yana-K38/test_TaskSQL_mindbox/tree/main

### Техническое задание
В PySpark приложении датафреймами (pyspark.sql.DataFrame) заданы продукты, категории и их связи. Каждому продукту может соответствовать несколько категорий или ни одной. А каждой категории может соответствовать несколько продуктов или ни одного. Напишите метод на PySpark, который в одном датафрейме вернет все пары «Имя продукта – Имя категории» и имена всех продуктов, у которых нет категорий.
### Решение 

Создаются DataFrames для Products, Categories со связью многие-ко-многим. Так же создается промежуточная таблица Product_categories,что бы хранить связи меджу Products и Categories.
```
Products
---------+-----------+
|productId|productName|
+---------+-----------+
|        1|  Product A|
|        2|  Product B|
|        3|  Product C|
|        4|  Product D|
+---------+-----------+
```
```
Categories
+----------+------------+
|categoryId|categoryName|
+----------+------------+
|         1|  Category X|
|         2|  Category Y|
|         3|  Category Z|
+----------+------------+
```
```
Product_categories
+----------+---------+
|categoryId|productId|
+----------+---------+
|         1|        1|
|         2|        1|
|         2|        2|
|         3|        3|
+----------+---------+
```

Выполняется SQL запрос на выборку всех пар ProductName - CategoryName, включая ProductName без категории.

```
SELECT p.productName, c.categoryName
    FROM products p
    LEFT JOIN product_categories pc ON p.productId = pc.productId
    LEFT JOIN categories c ON pc.categoryId = c.categoryId
```
Вывод
```
+-----------+------------+
|productName|categoryName|
+-----------+------------+
|  Product D|        null|
|  Product A|  Category X|
|  Product C|  Category Z|
|  Product A|  Category Y|
|  Product B|  Category Y|
+-----------+------------+
```
