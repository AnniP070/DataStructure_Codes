class Node: 
    def __init__(self, task, priority): 
        self.task = task 
        self.priority = priority 
        self.next = None 
 
class ToDoList: 
    def __init__(self): 
        self.head = None 
 
    def push(self, task, priority): 
        new_node = Node(task, priority) 
        priority_levels = {"high": 1, "medium": 2, "low": 3} 
 
        if self.head is None or priority_levels[priority] < priority_levels[self.head.priority]: 
            new_node.next = self.head 
            self.head = new_node 
        else: 
            current = self.head 
            while current.next is not None and priority_levels[priority] >= priority_levels[current.next.priority]: 
                current = current.next 
            new_node.next = current.next 
            current.next = new_node 
 
    def display(self): 
        if self.head is None: 
            print("No tasks in the list.") 
            return 
        current = self.head 
        while current is not None: 
            print(f"Task: {current.task}, Priority: {current.priority}") 
            current = current.next 
 
    def pop(self): 
        if self.head is None: 
            print("No tasks to pop.") 
            return 
        remove_task = self.head 
        self.head = self.head.next 
        print(f"Popped task: {remove_task.task}, Priority: {remove_task.priority}") 
 
    def peek(self): 
        if self.head is None: 
            print("No tasks in the list.") 
            return 
        print(f"Task: {self.head.task}, Priority: {self.head.priority}") 
 
def main(): 
    t = ToDoList() 
    
    t.push("Complete project proposal", "high") 
    t.push("Schedule team meeting", "medium") 
    t.push("Review draft presentation", "low") 
    t.push("Prepare weekly report", "high") 
    t.push("Respond to client", "medium") 
 
    while True: 
        print("\nTo-Do List Options:") 
        print("1. Add a task (push)") 
        print("2. Remove the highest priority task (pop)") 
        print("3. View the highest priority task (peek)") 
        print("4. Display all tasks") 
        print("5. Exit") 
 
        choice = input("Enter your choice: ") 
 
        if choice == '1': 
            task = input("Enter the task: ") 
            priority = input("Enter the priority (high, medium, low): ").lower() 
            t.push(task, priority) 
 
        elif choice == '2': 
            t.pop() 
 
        elif choice == '3': 
            t.peek() 
 
        elif choice == '4': 
            t.display() 
 
        elif choice == '5': 
            print("Exiting...") 
            break 
 
        else: 
            print("Invalid choice. Please try again.") 
 
if __name__ == "__main__": 
    main()