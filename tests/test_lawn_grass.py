from src.products import LawnGrass


def test_init():
    grass = LawnGrass(
        name="name",
        description="description",
        price=12.3,
        quantity=12,
        country="Russia",
        germination_period="7 days",
        color="red",
    )
    assert grass.name == "name"
    assert grass.description == "description"
    assert grass.price == 12.3
    assert grass.quantity == 12
    assert grass.country == "Russia"
    assert grass.germination_period == "7 days"
    assert grass.color == "red"
