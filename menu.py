"""
GitHub repository: https://github.com/Andrusyshyn-Orest/logistic_system.git
"""

import sys

from logistic_system import Item, Vehicle, Location, Order, LogisticSystem

id_of_item = 0

class Menu:
    '''Display a menu and respond to choices when run.'''

    def __init__(self):
        self.username = None
        self.city = None
        self.postoffice = None
        self.cart = []
        self.vehicles = []
        self.logisticsystem = None
        self.choices = {
                "1": self.show_available_items,
                "2": self.show_cart,
                "3": self.add_item_to_cart,
                "4": self.remove_item_from_cart,
                "5": self.place_order,
                "6": self.track_order,
                "7": self.quit
                }
        self.available_items = {
                "1": ("flowers", 11),
                "2": ("shoes", 153),
                "3": ("helicopter", 0.33),
                "4": ("book", 110),
                "5": ("chupachups", 44),
                "6": ("coat", 61.8),
                "7": ("shower", 5070),
                "8": ("rollers", 700),
                "9": ("powerbank", 900),
                "10": ("phone", 7458.50)
                }

    def display_menu(self):
        """
        """
        print("""

Menu
1. Show available items
2. Show cart
3. Add to cart
4. Remove from cart
5. Place order
6. Track order
7. Quit
""")

    def run(self):
        '''Display the menu and respond to choices.'''
        try:
            numbers = input('Enter vehicle numbers separated with\
    space (f.e.: 1 2 3):').split()
            numbers = set(numbers)
            for number in numbers:
                self.vehicles.append(Vehicle(int(number)))
        except:
            print("Invalid input")
            sys.exit(0)

        username = input('Enter your username: ')
        city = input('Enter your city: ')
        postoffice = input('Enter number of your postoffice: ')
        self.username = username
        self.city = city
        try:
            self.postoffice = int(postoffice)
        except:
            print("Invalid number of postoffice")
            sys.exit(0)
        self.logisticsystem = LogisticSystem(self.vehicles)

        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def show_available_items(self, notes=None):
        """
        """

        print("""

Available items:
1. flowers, 11 UAH
2. shoes, 153 UAH
3. helicopter, 0.33 UAH
4. book, 110 UAH
5. chupachups, 44 UAH
6. coat, 61.8 UAH
7. shower, 5070 UAH
8. rollers, 700 UAH
9. powerbank, 900 UAH
10. phone, 7458.50 UAH
""")

    def show_cart(self):
        """
        """

        if not self.cart:
            print('Cart is empty')
        else:
            for item in self.cart:
                print(f'id: {item[1]}; {item[2][0]}, {item[2][1]} UAH')

    def add_item_to_cart(self):
        """
        """

        choice = input('Enter item number:')
        item_tuple = self.available_items.get(choice)
        if item_tuple:
            name = item_tuple[0]
            price = item_tuple[1]
            global id_of_item
            id_of_item += 1
            self.cart.append( (Item(name, price), id_of_item, item_tuple) )
        else:
            print("{0} is not a valid choice".format(choice))

    def remove_item_from_cart(self):
        """
        """

        choice = input('Enter item id:')
        success = False
        for item in self.cart.copy():
            if str(item[1]) == choice:
                self.cart.remove(item)
                success = True
                break
        if not success:
            print("{0} is not a valid choice".format(choice))

    def place_order(self):
        """
        """

        my_items = []
        for item in self.cart:
            my_items.append(item[0])
        my_order = Order(self.username, self.city, self.postoffice, my_items)
        self.logisticsystem.placeOrder(my_order)


    def track_order(self):
        """
        """


        try:
            order_number = int(input('Enter order number: '))
            self.logisticsystem.trackOrder(order_number)
        except:
            print("Invalid order number")

    def quit(self):
        """
        """
        print("Thank you for using our program.")
        sys.exit(0)


if __name__ == "__main__":
    Menu().run()
