# Mock-Code-Coffee-shop


# Coffee Shop Classes

This project models a simple coffee shop system using three classes: `Customer`, `Coffee`, and `Order`. These classes represent customers, coffee types, and orders in the system, respectively.

## Classes and Methods

### Customer
- `__init__(name: str)`: Initializes a customer with a name.
- `name`: Property to get or set the customer's name (1-15 characters).
- `orders() -> list`: Returns all orders associated with the customer.
- `coffees() -> list`: Returns unique coffees the customer has ordered.
- `create_order(coffee: Coffee, price: float) -> Order`: Creates a new order for the customer.

### Coffee
- `__init__(name: str)`: Initializes a coffee with a name (minimum 3 characters).
- `name`: Property to get the coffee's name (immutable).
- `orders() -> list`: Returns all orders associated with this coffee.
- `customers() -> list`: Returns unique customers who ordered this coffee.
- `num_orders() -> int`: Returns the total number of orders for this coffee.
- `average_price() -> float`: Calculates the average price of this coffee based on orders.

### Order
- `__init__(customer: Customer, coffee: Coffee, price: float)`: Initializes an order with a customer, coffee, and price (1.0-10.0).
- `price`: Property to get the order's price.
- `customer`: Property to get the customer associated with the order.
- `coffee`: Property to get the coffee associated with the order.

## Example Usage
```python
# Create customers
customer1 = Customer("Alice")
customer2 = Customer("Bob")

# Create coffees
coffee1 = Coffee("Espresso")
coffee2 = Coffee("Latte")

# Create orders
order1 = customer1.create_order(coffee1, 5.5)
order2 = customer1.create_order(coffee2, 4.5)
order3 = customer2.create_order(coffee1, 6.0)

# Inspect data
print(f"Customer {customer1.name} has ordered: {[coffee.name for coffee in customer1.coffees()]}")
print(f"Coffee {coffee1.name} has {coffee1.num_orders()} orders with an average price of {coffee1.average_price():.2f}")
```

## Running the Code
Run the script directly to see the example usage in action.

## Notes
- The `Customer` and `Coffee` classes ensure data integrity with strict validations.
- Orders are stored at the class level in the `Order` class to enable global tracking.

"""
