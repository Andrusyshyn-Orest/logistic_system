"""
This module contains classes: Location, Item, Vehicle, Order, LogisticSystem.
GitHub repository: https://github.com/Andrusyshyn-Orest/logistic_system.git
"""

from typing import List

class Location:
    """
    Represent a location of post office.
    """

    def __init__(self, city: str, postoffice: int):
        """
        Initialize the location by its city and post office number.
        """
        self.city = city
        self.postoffice = postoffice


class Item:
    """
    Represent an item which can be ordered.
    """

    def __init__(self, name: str, price: float):
        """ Initialize an item by its name and price """
        self.name = name
        self.price = price

    def __str__(self):
        """
        Represent an item as follow:

        >>> item = Item('bike', 15000)
        >>> print(item)
        Your item is bike. It costs 15000 UAH.
        """
        return f'Your item is {self.name}. It costs {self.price} UAH.'


isAvailable = True

class Vehicle:
    """
    Represent a vehicle.
    """

    def __init__(self, vehicleNo: int):
        """ Initialize a vehicle by its Nomer """
        self.vehicleNo = vehicleNo
        global isAvailable
        self.isAvailable = isAvailable

order_id = 0

class Order:
    """
    Represent an order.
    """

    def __init__(self, user_name: str, city: str,
                 postoffice: int, items: List[Item]):
        """
        Initialize an order with name of a user (user_name),
        city, number of postoffice (postoffice), items and order id
        """

        if items != []:
            global order_id
            order_id += 1
            self.order_id = order_id
        self.user_name = user_name
        self.location = Location(city, postoffice)
        self.items = items
        self.vehicle = None
        print(self)

    def __str__(self):
        """
        Represent an order as follow:

        >>> item = Item('bike', 15000)
        >>> order = Order('Orest', 'Lviv', 73, [item])
        Your order number is 2.
        >>> print(order)
        Your order number is 2.
        """

        try:
            return f'Your order number is {self.order_id}.'
        except:
            return 'Your order is empty. You need to order at least one item.'

    def calculateAmount(self) -> float:
        """
        Return total price of items.

        >>> item = Item('bike', 15000)
        >>> item1 = Item('bike', 15000)
        >>> order = Order('Orest', 'Lviv', 73, [item, item1])
        Your order number is 4.
        >>> order.calculateAmount()
        30000
        """

        amount = 0
        for item in self.items:
            amount += item.price
        return amount

    def assignVehicle(self, vehicle: Vehicle):
        """
        Assign a vehicle for an order.

        >>> item = Item('bike', 15000)
        >>> order = Order('Orest', 'Lviv', 73, [item])
        Your order number is 3.
        >>> vehicle = Vehicle(3)
        >>> order.assignVehicle(vehicle)
        >>> order.vehicle.vehicleNo
        3
        """

        self.vehicle = vehicle


class LogisticSystem:
    """
    Represent logistic system for orders.
    """

    def __init__(self, vehicles: List[Vehicle]):
        """
        Initialize logistic system with an empty list of orders
        and list of vehicles.
        """
        self.orders = []
        self.vehicles = vehicles

    def placeOrder(self, order: Order):
        """
        Place an order.
        """

        if order.items == []:
            return

        success = False
        for vehicle in self.vehicles:
            if vehicle.isAvailable:
                success = True
                vehicle.isAvailable = False
                order.vehicle = vehicle
                self.orders.append(order)
                # print(order)
                break
        if not success:
            print('There is no available vehicle to deliver an order.')

    def trackOrder(self, orderid : int) -> str:
        """
        Track an order.

        >>> item = Item('bike', 15000)
        >>> order = Order('Orest', 'Lviv', 73, [item])
        Your order number is 1.
        >>> vehicle = Vehicle(2)
        >>> logsystem = LogisticSystem([vehicle])
        >>> logsystem.placeOrder(order)
        >>> logsystem.trackOrder(1)
        Your order #1 is sent to Lviv. Total price: 15000 UAH.
        """

        success = False
        for order in self.orders:
            if order.order_id == orderid:
                print(
f'Your order #{orderid} is sent to {order.location.city}. Total price:\
 {order.calculateAmount()} UAH.'
)
                success = True
                break
        if not success:
            print("No such order.")


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
