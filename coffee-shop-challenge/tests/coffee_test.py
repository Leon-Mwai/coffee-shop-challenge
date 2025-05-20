import pytest
from src.coffee import Coffee


def test_coffee_name_getter_and_immutable():
    coffee = Coffee("Mocha")
    assert coffee.name == "Mocha"

    with pytest.raises(AttributeError):
        coffee.name = "Latte"  

def test_coffee_orders_and_customers():
    coffee = Coffee("Americano")
    cust1 = Customer("Leon")
    cust2 = Customer("Alice")

    assert coffee.orders() == []
    assert coffee.customers() == []

    cust1.create_order(coffee, 3.5)
    cust2.create_order(coffee, 4.0)

    assert len(coffee.orders()) == 2
    assert set(coffee.customers()) == {cust1, cust2}

def test_coffee_num_orders_and_average_price():
    coffee = Coffee("Cappuccino")
    cust = Customer("Leon")

    assert coffee.num_orders() == 0
    assert coffee.average_price() == 0

    cust.create_order(coffee, 4.0)
    cust.create_order(coffee, 6.0)

    assert coffee.num_orders() == 2
    assert coffee.average_price() == 5.0
