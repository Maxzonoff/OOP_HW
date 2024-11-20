import pytest

from src.products import LawnGrass, Product, Smartphone


def test_product_init():
    """Тест для инициализации"""
    name = "Iphone 15"
    description = "512GB, Gray space"
    price = 210000
    quantity = 8

    product = Product(name, description, price, quantity)
    assert product.name == "Iphone 15"
    assert product.description == "512GB, Gray space"
    assert product.price == 210000
    assert product.quantity == 8


def test_product_quantity_zero():
    """Тест на выброс исключения при нулевом количестве продукта"""
    with pytest.raises(
        ValueError, match="Товар с нулевым количеством не может быть добавлен"
    ):
        Product("Iphone 15", "512GB, Gray space", 210000, 0)


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
        "name": "Iphone 15",
        "description": "512GB, Gray space",
        "price": 210000,
        "quantity": 8,
    }

    product = Product.new_product(params)

    assert product.name == "Iphone 15"
    assert product.description == "512GB, Gray space"
    assert product.price == 210000
    assert product.quantity == 8


def test_add():
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    assert product1 + product2 == 2580000.0


def test_price_setter():
    """Тест для сеттера атрибута 'price'"""
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


def test_add_different_categories_raises_error():
    """Тест сложение разных категорий выкидывает ошибку"""
    smartphone = Smartphone(
        name="name",
        description="description",
        price=12.2,
        quantity=12,
        efficiency=12.5,
        model="12",
        memory=128,
        color="red",
    )
    lawn_grass = LawnGrass(
        name="name",
        description="description",
        price=12.2,
        quantity=12,
        country="Russia",
        germination_period="7 дней",
        color="Зеленый",
    )
    with pytest.raises(TypeError):
        smartphone + lawn_grass
