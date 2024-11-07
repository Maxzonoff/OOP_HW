import pytest

from src.products import Category, Product


def test_product_init():
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