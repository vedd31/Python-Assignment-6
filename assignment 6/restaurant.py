from menu import Menu
from exceptions import CustomException

def main():
    menu = Menu()
    menu.read_menu_from_file()

    while True:
        print("\nRestaurant Management System")
        print("1. Add Menu Item")
        print("2. Update Menu Item")
        print("3. Delete Menu Item")
        print("4. Display Menu")
        print("5. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == '1':
                name = input("Enter item name: ")
                price = float(input("Enter item price: "))
                quantity = int(input("Enter item quantity: "))
                menu.add_item(name, price, quantity)
                print("Item added successfully.")
            elif choice == '2':
                name = input("Enter item name: ")
                price = float(input("Enter item price: "))
                quantity = int(input("Enter item quantity: "))
                menu.update_item(name, price, quantity)
                print("Item updated successfully.")
            elif choice == '3':
                name = input("Enter item name: ")
                menu.delete_item(name)
                print("Item deleted successfully.")
            elif choice == '4':
                menu.display_menu()
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please try again.")
        except CustomException as e:
            print(e)

if __name__ == "__main__":
    main()