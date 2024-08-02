from exceptions import InvalidMenuItemError

class MenuItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def _repr_(self):
        return f"{self.name},{self.price},{self.quantity}"

class Menu:
    def __init__(self):
        self.items = []
        self.read_menu_from_file()  # Ensure the menu is loaded at initialization

    def add_item(self, name, price, quantity):
        if self.find_item(name):
            raise InvalidMenuItemError(f"Menu item '{name}' already exists.")
        self.items.append(MenuItem(name, price, quantity))
        self.write_menu_to_file()

    def update_item(self, name, price, quantity):
        item = self.find_item(name)
        if item:
            item.price = price
            item.quantity = quantity
            self.write_menu_to_file()
        else:
            raise InvalidMenuItemError(f"Menu item '{name}' does not exist.")

    def delete_item(self, name):
        item = self.find_item(name)
        if item:
            self.items.remove(item)
            self.write_menu_to_file()
        else:
            raise InvalidMenuItemError(f"Menu item '{name}' does not exist.")

    def display_menu(self):
        if not self.items:
            print("No items in the menu.")
        else:
            for item in self.items:
                print(f"Name: {item.name}, Price: {item.price}, Quantity: {item.quantity}")

    def find_item(self, name):
        for item in self.items:
            if item.name == name:
                return item
        return None

    def read_menu_from_file(self):
        try:
            with open('menu.txt', 'r') as file:
                lines = file.readlines()
                self.items = []
                for line in lines:
                    name, price, quantity = line.strip().split(',')
                    self.items.append(MenuItem(name, float(price), int(quantity)))
        except FileNotFoundError:
            self.items = []

    def write_menu_to_file(self):
        with open('menu.txt', 'w') as file:
            for item in self.items:
                file.write(f"{item.name},{item.price},{item.quantity}\n")

# Load initial menu from file
menu = Menu()
menu.read_menu_from_file()