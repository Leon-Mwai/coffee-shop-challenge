import pytest
from src.customer import Customer
from src.order import Order


def test_customer_name_getter_and_setter():
    cust = Customer("Leon")
    assert cust.name == "Leon"

    cust.name = "Alice"
    assert cust.name == "Alice"

    with pytest.raises(TypeError):
        cust.name = 123  

    with pytest.raises(ValueError):
        cust.name = ""  

    with pytest.raises(ValueError):
        cust.name = "a" * 16  

def test_customer_orders_and_coffees():
    cust = Customer("Leon")
    coffee1 = Coffee("Latte")
    coffee2 = Coffee("Espresso")

    # No orders yet
    assert cust.orders() == []
    assert cust.coffees() == []

    # Create orders
    order1 = cust.create_order(coffee1, 4.0)
    order2 = cust.create_order(coffee2, 5.5)
    order3 = cust.create_order(coffee1, 3.0)

    assert len(cust.orders()) == 3
    assert set(cust.coffees()) == {coffee1, coffee2}
