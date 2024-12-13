class Node: 
    def __init__(self,id,name,items): 
        self.name=name 
        self.id=id 
        self.items=[] 
        for element in items: 
            self.items.append(element) 
        self.next=None 
 
class Orders: 
    def __init__(self): 
        self.front=None 
        self.rear=None 
 
    def addOrder(self): 
        id=int(input("Enter Order ID ")) 
        name=input("Enter name of customer ") 
        items=[] 
        again=True 
        while again : 
            add_items=int(input("1. To add item\n2.Done.\nEnter choice")) 
            if add_items==1: 
                item=input("Enter item name ") 
                items.append(item) 
            elif add_items==2: 
                again=False 
            else: 
                print("Enter valid choice") 
        newNode=Node(id,name,items) 
 
        if self.front==None and self.rear==None: 
            self.front=newNode 
            self.rear=newNode 
            self.rear.next=self.front 
            return 
        else: 
            self.rear.next=newNode 
            newNode.next=self.front 
            self.rear=newNode 
            return 
 
    def removeOrder(self): 
        if self.front==None : 
            print("No orders") 
        elif self.front==self.rear: 
            temp=self.front 
            self.front=None 
            self.rear=None 
            print(f"{temp.name}'s order is removed.") 
        else: 
            temp=self.front 
            self.front=self.front.next 
            print(f"{temp.name}'s order is removed.") 
            temp=None 
            self.rear.next=self.front 
 
    def display(self): 
        current=self.front 
        if current==None: 
            print("List is empty") 
            return 
        print("Order ID : ", current.id) 
        print("Items : ", current.items) 
        print("Customer name : ", current.name) 
        current=current.next 
        while current!=self.front: 
            print("Order ID : ", current.id) 
            print("Items : ", current.items) 
            print("Customer name : ", current.name) 
            current=current.next 
        print("\n\n") 
        print("End\n\n") 
 
 
if __name__=="__main__": 
    print("Welcome to our Restaurant") 
    repeat=True 
    O=Orders() 
    while repeat : 
        choice=int(input("1. To Add Order\n2. To Remove Order\n3. To Display Order List\n4. Exit\nEnter choice ")) 
        if choice==1: 
            O.addOrder() 
            print("Order added successfully.") 
        elif choice==2: 
            O.removeOrder() 
        elif choice==3: 
            O.display() 
        elif choice==4: 
            repeat=False 
        else: 
            print("Enter valid choice") 
 
 
