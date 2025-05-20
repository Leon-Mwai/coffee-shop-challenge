import pytest
from src.customer import Customer
from src.order import Order

def test_order_init_and_properties():
    cust = Customer("Leon")
    coffee = Coffee("Espresso")
    order = Order(cust, coffee, 5.5)

    assert order.customer == cust
    assert order.coffee == coffee
    assert order.price == 5.5

def test_order_price_immutable_and_validation():
    cust = Customer("Leon")
    coffee = Coffee("Espresso")

 
    with pytest.raises(ValueError):
        Order(cust, coffee, 0.5)

    with pytest.raises(ValueError):
        Order(cust, coffee, 11.0)

   
    with pytest.raises(TypeError):
        Order(cust, coffee, "five")

   
    order = Order(cust, coffee, 5.0)
    with pytest.raises(AttributeError):
        order.price = 6.0

def test_order_customer_and_coffee_typecheck():
    coffee = Coffee("Latte")
    cust = Customer("Alice")

    with pytest.raises(TypeError):
        Order("not a customer", coffee, 5.0)

    with pytest.raises(TypeError):
        Order(cust, "not a coffee", 5.0)
