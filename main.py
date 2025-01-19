class Customer:

    #initializing the customer with a name

    def __init__(self, name):
        self.name = name

    # getter for the name 
    @property
    def name(self):
        return self._name 

    #setter for the name property
    @name.setter
    def name(self, value):


        if not isinstance(value, str):
            raise TypeError("Name must be a string.")
        if not (1 <= len(value) <= 15):
            raise ValueError("Name must be between 1 and 15 characters.")
        self._name = value

        #return a list of all arders associated with the customer

        def orders(self):
            return [order for order in Order._all_orders if order.customer == self]
        

        #return a list of coffee the customer ordered
        def coffees(self):
            return list ({order.coffee for order in self.orders()})
        

        #create a new order for the customeer
        def create_order(self, coffee, price):
            return Order(self, coffee, price)
        


class Coffee:
    #initialize the coffe with a name
    def __init__(self, name):

        if not isinstance(name, str):
            raise TypeError("Name must be a string.")

        if len(name) < 3:
            raise ValueError("Name must be at least 3 characters long.")

        if hasattr(self, "_name"):
            raise AttributeError("Name can't be changed once set.")

        self._name = name


        #getter 4 name property
        # 
        @property
        def name(self):
            return self._name
        

        #return a list of all orders 4 this coffee
        def orders(self):
            return [order for order in Order._all_orders if order.coffee == self]
        

        #return list of customers that ordered that coffee
        def customers(self):
            return list({order.customer for order in self.orders()})
        

        #returns the total number of orders for this coffee
        def num_orders(self):
            return len(self.orders())
        
        #calculate the avaerage price of this coffee based on the orders

        def average_price(self):
            orders = self.orders()

            if not orders:
                return sum(order.price for order in orders) / len(orders)
            

class Order:
    # class-level list to store all orders
    _all_orders = []


    #initialize the order with a customer, coffee and price
    def __init__(self, customer, coffee, price):

        if not isinstance(customer, Customer):
            raise TypeError("Customer must be an instance of Customer.")
        
        if not isinstance(coffee, Coffee):
            raise TypeError("Coffee must be an instance of coffee.")
        
        if not isinstance(price, (int,float)) or not (1.0 <= price <= 10.0):
            raise ValueError("Price must be a float between 1.0 and 10.0.")
        

        self._customer = customer
        self._coffee = coffee
        self._price = float(price)
        Order._all_orders.append(self)




        #getter 4 the price property
        @property 
        def price (self):
            return self._price
        

        #getter for the customer 

        @property
        def customer(self):
            return self.customer
        


        #getter for the coffee 
        @property
        def coffee(self):
            return self._coffee
        
        #usage 



if __name__ == "__main__":
    # Create customers
    customer1 = Customer("Alice")
    customer2 = Customer("Bob")

    # Create coffees
    coffee1 = Coffee("Espresso")
    coffee2 = Coffee("Latte")

    # Create orders
    
    order2 = customer1.create_order(coffee2, 4.5)
    order3 = customer2.create_order(coffee1, 6.0)

    # Inspect data
    print(f"Customer {customer1.name} has ordered: {[coffee.name for coffee in customer1.coffees()]}")
    print(f"Coffee {coffee1.name} has {coffee1.num_orders()} orders with an average price of {coffee1.average_price():.2f}")



    


    


                

                
            