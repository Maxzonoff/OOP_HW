from src.products import Smartphone


def test_init():
    smartphone = Smartphone(
        name="name",
        description="description",
        price=12.3,
        quantity=12,
        efficiency=12.5,
        model="12",
        memory=128,
        color="red",
    )
    assert smartphone.name == "name"
    assert smartphone.description == "description"
    assert smartphone.price == 12.3
    assert smartphone.quantity == 12
    assert smartphone.efficiency == 12.5
    assert smartphone.model == "12"
    assert smartphone.memory == 128
    assert smartphone.color == "red"
