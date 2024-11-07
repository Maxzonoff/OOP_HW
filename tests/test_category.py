from src.products import Category, Product


def test_category_init():
    """Тест для инициализации"""
    name = "фрукты"
    description = "категория фруктов"
    Category.category_count = 0
    products = [
        Product("яблоко", "описание яблока", 10, 2),
        Product("груша", "описание груши", 15, 4),
    ]

    category = Category(name, description, products)

    assert category.name == "фрукты"
    assert category.description == "категория фруктов"
    assert Category.product_count == 2
    assert Category.category_count == 1


def test_str():
    name = "Смартфоны"
    description = "категория смартфонов"
    products = [
        Product(
            "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
        ),
        Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
        Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14),
    ]
    category = Category(name, description, products)
    assert str(category) == "Смартфоны, количество продуктов: 27 шт."


def test_add_product():
    """Тест для метода add_product"""
    name = "фрукты"
    description = "категория фруктов"
    Category.category_count = 0
    Category.product_count = 0
    product_to_add = Product("слива", "описание сливы", 25, 6)
    products = [
        Product("яблоко", "описание яблока", 10, 2),
        Product("груша", "описание груши", 15, 4),
    ]
    category = Category(name, description, products)

    category.add_product(product_to_add)

    assert Category.product_count == 3


def test_products():
    """Тест для метода products"""
    name = "фрукты"
    description = "категория фруктов"
    Category.category_count = 0
    Category.product_count = 0
    product_to_add = Product("слива", "описание сливы", 25, 6)
    products = [
        Product("яблоко", "описание яблока", 10, 2),
        Product("груша", "описание груши", 15, 4),
    ]
    category = Category(name, description, products)

    assert (
        category.products
        == "яблоко, 10 руб. Остаток: 2 шт. груша, 15 руб. Остаток: 4 шт."
    )
    category.add_product(product_to_add)
    assert (
        category.products
        == "яблоко, 10 руб. Остаток: 2 шт. груша, 15 руб. Остаток: 4 шт. слива, 25 руб. Остаток: 6 шт."
    )
