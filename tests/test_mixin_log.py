from src.products import LawnGrass, Product, Smartphone


def test_product_mixin_log(capsys):
    Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    captured = capsys.readouterr()
    assert (
        captured.out
        == "Product(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)\n"
    )


def test_lawng_rass_mixin_log(capsys):
    LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )
    captured = capsys.readouterr()
    assert (
        captured.out
        == "LawnGrass(Газонная трава, Элитная трава для газона, 500.0, 20, Россия, 7 дней, Зеленый)\n"
    )


def test_smartphone_mixin_log(capsys):
    Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 5.5, "15", 512, "red")
    captured = capsys.readouterr()
    assert (
        captured.out
        == "Smartphone(Iphone 15, 512GB, Gray space, 210000.0, 8, 5.5, 15, 512, red)\n"
    )
