# Define the inventory list
inventory = []


def add_item():

    name = input("Enter the item name: ")
    price = float(input("Enter the item price: "))
    quantity = int(input("Enter the item quantity: "))
    category = input("Enter the item category: ")


    item = {
        'name': name,
        'price': price,
        'quantity': quantity,
        'category': category
    }
    inventory.append(item)
    print(f"Item '{name}' added successfully.")


def update_item():

    name = input("Enter the name of the item to update: ")


    item = next((item for item in inventory if item['name'] == name), None)

    if item:
        print(f"Updating item '{name}'")
        item['price'] = float(input("Enter the new price: "))
        item['quantity'] = int(input("Enter the new quantity: "))
        item['category'] = input("Enter the new category: ")
        print(f"Item '{name}' updated successfully.")
    else:
        print(f"Item '{name}' not found.")


def view_inventory():

    if not inventory:
        print("The inventory is empty.")
        return

    print(f"{'Name':<20} {'Price':<10} {'Quantity':<10} {'Category':<15}")
    print("-" * 55)

    for item in inventory:
        print(f"{item['name']:<20} {item['price']:<10.2f} {item['quantity']:<10} {item['category']:<15}")


def remove_item():

    name = input("Enter the name of the item to remove: ")

    global inventory
    inventory = [item for item in inventory if item['name'] != name]

    print(f"Item '{name}' removed successfully.")


def search_by_category():

    category = input("Enter the category to search for: ")

    items_found = [item for item in inventory if item['category'].lower() == category.lower()]

    if not items_found:
        print(f"No items found in category '{category}'.")
        return

    print(f"Items in category '{category}':")
    print(f"{'Name':<20} {'Price':<10} {'Quantity':<10}")
    print("-" * 50)

    for item in items_found:
        print(f"{item['name']:<20} {item['price']:<10.2f} {item['quantity']:<10}")


def main():

    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. Update Item")
        print("3. View Inventory")
        print("4. Remove Item")
        print("5. Search by Category")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_item()
        elif choice == '2':
            update_item()
        elif choice == '3':
            view_inventory()
        elif choice == '4':
            remove_item()
        elif choice == '5':
            search_by_category()
        elif choice == '6':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")



