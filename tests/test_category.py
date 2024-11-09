import pytest

from src.products import Category, Product
# from src.read_json import category


#
#
# def test_category_init():
#     """Тест для инициализации"""
#     name = "фрукты"
#     description = "категория фруктов"
#     Category.category_count = 0
#     products = [
#         Product("яблоко", "описание яблока", 10, 2),
#         Product("груша", "описание груши", 15, 4),
#     ]
#
#     category = Category(name, description, products)
#
#     assert category.name == "фрукты"
#     assert category.description == "категория фруктов"
#     assert Category.product_count == 2
#     assert Category.category_count == 1
#
#
# def test_add_product():
#     """Тест для метода add_product"""
#     name = "фрукты"
#     description = "категория фруктов"
#     Category.category_count = 0
#     Category.product_count = 0
#     product_to_add = Product("слива", "описание сливы", 25, 6)
#     products = [
#         Product("яблоко", "описание яблока", 10, 2),
#         Product("груша", "описание груши", 15, 4),
#     ]
#     category = Category(name, description, products)
#
#     category.add_product(product_to_add)
#
#     assert Category.product_count == 3
#
#
# def test_products():
#     """Тест для метода products"""
#     name = "фрукты"
#     description = "категория фруктов"
#     Category.category_count = 0
#     Category.product_count = 0
#     product_to_add = Product("слива", "описание сливы", 25, 6)
#     products = [
#         Product("яблоко", "описание яблока", 10, 2),
#         Product("груша", "описание груши", 15, 4),
#     ]
#     category = Category(name, description, products)
#
#     assert (
#         category.products
#         == "яблоко, 10 руб. Остаток: 2 шт. груша, 15 руб. Остаток: 4 шт."
#     )
#     category.add_product(product_to_add)
#     assert (
#         category.products
#         == "яблоко, 10 руб. Остаток: 2 шт. груша, 15 руб. Остаток: 4 шт. слива, 25 руб. Остаток: 6 шт."
#     )


def test_cant_add_if_not_subclass_of_product():
    """ Тест нельзя добавлять не подклассы класса Product """
    category = Category(
        name='name',
        description='описание',
        products=[]
    )
    with pytest.raises(ValueError):
        category.add_product(123)
