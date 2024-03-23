from pyspark.sql import SparkSession
# from pyspark.sql.functions import col


spark = SparkSession.builder.appName("ProductCategory").getOrCreate()

products = spark.createDataFrame([
    {"productId": 1, "productName": "Product A"},
    {"productId": 2, "productName": "Product B"},
    {"productId": 3, "productName": "Product C"},
    {"productId": 4, "productName": "Product D"},
])

categories = spark.createDataFrame([
    {"categoryId": 1, "categoryName": "Category X"},
    {"categoryId": 2, "categoryName": "Category Y"},
    {"categoryId": 3, "categoryName": "Category Z"},
])

product_categories = spark.createDataFrame([
    {"productId": 1, "categoryId": 1},
    {"productId": 1, "categoryId": 2},
    {"productId": 2, "categoryId": 2},
    {"productId": 3, "categoryId": 3},
])

products.createOrReplaceTempView("products")
products.show()
categories.createOrReplaceTempView("categories")
categories.show()
product_categories.createOrReplaceTempView("product_categories")
product_categories.show()

result_df = spark.sql("""
    SELECT p.productName, c.categoryName
    FROM products p
    LEFT JOIN product_categories pc ON p.productId = pc.productId
    LEFT JOIN categories c ON pc.categoryId = c.categoryId
""")

result_df.show()