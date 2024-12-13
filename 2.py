class ProductNode: 
    def __init__(self, product_id, name, quantity, price, amount): 
        self.product_id = product_id 
        self.name = name 
        self.quantity = quantity 
        self.price = price 
        self.amount = amount 
        self.prev = None 
        self.next = None 
 
class InventoryManagement: 
    def __init__(self): 
        self.head = None 
        self.tail = None 
 
    # Add new product at the end of the doubly linked list 
    def add_product(self, product_id, name, quantity, price, amount): 
        new_product = ProductNode(product_id, name, quantity, price, amount) 
        if self.head is None: 
            self.head = new_product 
            self.tail = new_product 
        else: 
            self.tail.next = new_product 
            new_product.prev = self.tail 
            self.tail = new_product 
        print(f"Product {name} added to the inventory.") 
 
    # Update the quantity of an existing product 
    def update_quantity(self, product_id, quantity): 
        current = self.head 
        while current: 
            if current.product_id == product_id: 
                current.quantity = quantity 
                print(f"Product {current.name}'s quantity updated to {quantity}.") 
                return 
            current = current.next 
        print("Product not found.") 

    # Calculate the total value of the inventory 
    def calculate_total_value(self): 
        total_value = 0 
        current = self.head 
        while current: 
            total_value += current.amount 
            current = current.next 
        print(f"Total inventory value: ${total_value}") 
        return total_value 

    # Display all products in the inventory 
    def display_inventory(self): 
        if self.head is None: 
            print("The inventory is empty.") 
            return 
        current = self.head 
        while current: 
            print(f"Product ID: {current.product_id}, Name: {current.name}, "
                  f"Quantity: {current.quantity}, Price: ${current.price}, "
                  f"Total Amount: ${current.amount}") 
            current = current.next 

# Menu-driven system 
def menu(): 
    print("\n--- Inventory Management System Menu ---") 
    print("1. Add a new product") 
    print("2. Update product quantity") 
    print("3. Display inventory") 
    print("4. Calculate total value of inventory") 
    print("5. Exit") 
    return int(input("Enter your choice: ")) 
 
# Main execution 
inventory = InventoryManagement() 
 
inventory.add_product(101, "Laptop", 50, 800, 40000) 
inventory.add_product(102, "Smartphone", 100, 500, 50000) 
inventory.add_product(103, "Tablet", 30, 400, 12000) 
 
while True: 
    choice = menu() 
 
    if choice == 1: 
        product_id = int(input("Enter Product ID: ")) 
        name = input("Enter Product Name: ") 
        quantity = int(input("Enter Quantity: ")) 
        price = float(input("Enter Price: ")) 
        amount = quantity * price 
        inventory.add_product(product_id, name, quantity, price, amount) 
 
    elif choice == 2: 
        product_id = int(input("Enter Product ID to update: ")) 
        quantity = int(input("Enter new Quantity: ")) 
        inventory.update_quantity(product_id, quantity) 
 
    elif choice == 3: 
        inventory.display_inventory() 
 
    elif choice == 4: 
        inventory.calculate_total_value() 

    elif choice == 5: 
        print("Exiting the system.") 
        break 
    else: 
        print("Invalid choice. Please try again.")
