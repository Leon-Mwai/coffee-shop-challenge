from src.coffee import Coffee
from src.customer import Customer
from src.order import Order



cust1 = Customer("Leon")
cust2 = Customer("Alice")

coffee1 = Coffee("Espresso")
coffee2 = Coffee("Latte")

cust1.create_order(coffee1, 4.5)
cust1.create_order(coffee2, 5.0)
cust2.create_order(coffee1, 3.5)


print("Espresso orders:", coffee1.num_orders())        

print("Leon’s coffees:", [coffee.name for coffee in cust1.coffees()])  

print("Espresso customers:", [cust.name for cust in coffee1.customers()])  