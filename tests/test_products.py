from src.products import Product


def test_product_init():
    """Тест для инициализации"""
    name = "яблоко"
    description = "описание яблока"
    price = 10
    quantity = 2

    product = Product(name, description, price, quantity)

    assert product.name == "яблоко"
    assert product.description == "описание яблока"
    assert product.price == 10
    assert product.quantity == 2


def test_str():
    name = "яблоко"
    description = "описание яблока"
    price = 10
    quantity = 2
    product = Product(name, description, price, quantity)

    assert str(product) == "яблоко, 10 руб. Остаток: 2 шт."


def test_new_product():
    """Тест для метода new_product"""
    params = {
        "name": "яблоко",
        "description": "описание яблока",
        "price": 10,
        "quantity": 2,
    }

    product = Product.new_product(params)

    assert product.name == "яблоко"
    assert product.description == "описание яблока"
    assert product.price == 10
    assert product.quantity == 2


def test_add():
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    assert product1 + product2 == 2580000.0


def test_price_setter():
    name = "яблоко"
    description = "описание яблока"
    price = 10
    quantity = 2
    product = Product(name, description, price, quantity)

    new_price = 15

    product.price = new_price

    assert product.price == new_price
    product.price = -1

    assert product.price == new_price
