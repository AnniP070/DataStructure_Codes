class Node: 
    def __init__(self, name, id, service): 
        self.name=name 
        self.id=id 
        self.service=service 
        self.next=None 
 
class List: 
    def __init__(self): 
        self.front=None 
        self.rear=None 
 
    def addService(self): 
        id=int(input("Request ID : ")) 
        name=input("Customer Name : ") 
        service=input("Service Type : ") 
        newNode=Node(name,id,service) 
 
        if self.front==None and self.rear==None: 
            self.front=newNode 
            self.rear=newNode 
            return 
        else: 
            self.rear.next=newNode 
            self.rear=newNode 
            return 
 
    def removeService(self): 
        if self.front==None: 
            print("List is empty") 
        elif self.front==self.rear: 
            temp=self.front 
            self.front=None 
            self.rear=None 
            print(f"{temp.name} is successfully removed from the list.") 
            return 
        else: 
            temp=self.front 
            self.front=self.front.next 
            print(f"{temp.name} is successfully removed from the list.") 
            return 
 
    def display(self): 
        if self.front==None: 
            print("No Customer") 
            return 
        current=self.front 
        print("Service Requests : ") 
        while current: 
            print(f"ID = {current.id},\n  Name = {current.name},\n  Service = {current.service}\n") 
            current=current.next 
if __name__=="__main__": 
    again=True 
    print("Welcome to Call center") 
    list=List() 
    while again: 
        choice=int(input("1.Add Customer\n2. Remove Customer\n3. Display Customer List\n4. Exit\nEnter what you want to do ")) 
        if choice==1: 
            list.addService() 
            print("Customer added successfully.") 
        elif choice==2: 
            list.removeService() 
        elif choice==3: 
            list.display() 
        elif choice==4: 
            again=False 
        else: 
            print("Enter valid choice")