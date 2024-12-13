class Node:
    def __init__(self, name, disease, priority):
        self.name = name
        self.disease = disease
        self.priority = priority
        self.next = None

class LinkList:
    def __init__(self):
        self.head = None

    def add_node(self):
        """Add a new patient node based on priority."""
        name = input("Enter name of patient: ")
        disease = input("Disease of patient: ")
        priority = input("Priority of patient [Severe / Intermediate / Mild]: ").capitalize()

        if priority not in ["Severe", "Intermediate", "Mild"]:
            print("Invalid priority. Please enter Severe, Intermediate, or Mild.")
            return

        if priority == "Severe":
            self.add_after_severe(name, disease, priority)
        elif priority == "Intermediate":
            self.add_after_intermediate(name, disease, priority)
        else:
            self.add_at_end(name, disease, priority)

    def add_after_severe(self, name, disease, priority):
        new_node = Node(name, disease, priority)
        if self.head is None or self.head.priority != "Severe":
            new_node.next = self.head
            self.head = new_node
            return

        current_node = self.head
        while current_node.next and current_node.next.priority == "Severe":
            current_node = current_node.next

        new_node.next = current_node.next
        current_node.next = new_node

    def add_after_intermediate(self, name, disease, priority):
        new_node = Node(name, disease, priority)
        if not self.head:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next and current_node.next.priority in ["Severe", "Intermediate"]:
            current_node = current_node.next

        new_node.next = current_node.next
        current_node.next = new_node

    def add_at_end(self, name, disease, priority):
        new_node = Node(name, disease, priority)
        if not self.head:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def search(self):
        """Search for a patient by name."""
        if not self.head:
            print("List is empty.")
            return

        search_name = input("Enter the name of patient: ")
        current_node = self.head
        while current_node:
            if current_node.name == search_name:
                print(f"Patient found: [{current_node.name}, {current_node.disease}, {current_node.priority}]")
                return
            current_node = current_node.next

        print(f"Patient {search_name} not found.")

    def display(self):
        """Display the list of patients."""
        if not self.head:
            print("The list is empty.")
            return

        current_node = self.head
        while current_node:
            print(f"[{current_node.name}, {current_node.disease}, {current_node.priority}] --> ", end="")
            current_node = current_node.next
        print("End")

    def delete_node(self):
        """Delete a patient by name."""
        if not self.head:
            print("List is empty.")
            return

        delete_name = input("Enter the name of patient to be deleted: ")
        current_node = self.head
        previous_node = None

        while current_node and current_node.name != delete_name:
            previous_node = current_node
            current_node = current_node.next

        if not current_node:
            print(f"Patient {delete_name} not found.")
            return

        if previous_node is None:  # Deleting the head node
            self.head = current_node.next
        else:
            previous_node.next = current_node.next

        print(f"Patient {delete_name} has been deleted.")

def menu():
    print("\n1. Add Patient")
    print("2. Search Patient")
    print("3. Display All Patients")
    print("4. Delete Patient")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if not choice.isdigit():
        return -1
    return int(choice)

def main():
    print("PATIENT MANAGEMENT SYSTEM")
    linked_list = LinkList()

    while True:
        choice = menu()
        if choice == 1:
            linked_list.add_node()
        elif choice == 2:
            linked_list.search()
        elif choice == 3:
            linked_list.display()
        elif choice == 4:
            linked_list.delete_node()
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
