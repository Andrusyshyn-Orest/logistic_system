"""
GitHub repository: https://github.com/Andrusyshyn-Orest/logistic_system.git
"""

from typing import List

class Location:
    """
    """

    def __init__(self, city: str, postoffice: int):
        self.city = city
        self.postoffice = postoffice


class Item:
    """
    """

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self):
        """
        """
        return f'Your item is {self.name}. It costs {self.price} UAH.'


isAvailable = True

class Vehicle:
    """
    """

    def __init__(self, vehicleNo: int):
        self.vehicleNo = vehicleNo
        global isAvailable
        self.isAvailable = isAvailable

order_id = 0

class Order:
    """
    """

    def __init__(self, user_name: str, city: str,
                 postoffice: int, items: List[Item]):
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
        """
        return f'Your order number is {self.order_id}.'

    def calculateAmount(self) -> float:
        """
        """

        amount = 0
        for item in self.items:
            amount += item.price
        return amount

    def assignVehicle(self, vehicle: Vehicle):
        """
        """

        self.vehicle = vehicle


class LogisticSystem:
    """
    """

    def __init__(self, vehicles: List[Vehicle]):
        self.orders = []
        self.vehicles = vehicles

    def placeOrder(self, order: Order):
        """
        """

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
    vehicles = [Vehicle(1), Vehicle(2)]
    logSystem = LogisticSystem(vehicles)
    my_items = [Item('book',110), Item('chupachups',44)]
    my_order = Order(user_name = 'Oleg', city = 'Lviv',
                      postoffice = 53, items = my_items)
    logSystem.placeOrder(my_order)
    logSystem.trackOrder(234976475)
