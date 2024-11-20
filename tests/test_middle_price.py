from src.products import Category, Product


def test_middle_price():
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны", "Категория смартфонов", [product1, product2, product3]
    )
    assert category1.middle_price() == 140333.33

    category1 = Category("Смартфоны", "Категория смартфонов", [])
    assert category1.middle_price() == 0
