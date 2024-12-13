class StudentRecord: 
    def __init__(self, student_id, name, age, major): 
        self.student_id = student_id 
        self.name = name 
        self.age = age 
        self.major = major 
 
    def __str__(self): 
        return f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Major: {self.major}" 
 
class StudentHashTable: 
    def __init__(self, size=10): 
        self.size = size 
        self.table = [[] for _ in range(size)] 
 
    def _hash_function(self, student_id): 
        return student_id % self.size 
 
    def add_student(self, student): 
        index = self._hash_function(student.student_id) 
        for existing_student in self.table[index]: 
            if existing_student.student_id == student.student_id: 
                print("Student with this ID already exists.") 
                return 
        self.table[index].append(student) 
        print("Student record added successfully.") 
 
    def retrieve_student(self, student_id): 
        index = self._hash_function(student_id) 
        for student in self.table[index]: 
            if student.student_id == student_id: 
                return student 
        return None 
 
    def delete_student(self, student_id): 
        index = self._hash_function(student_id) 
        for i, student in enumerate(self.table[index]): 
            if student.student_id == student_id: 
                del self.table[index][i] 
                print("Student record deleted successfully.") 
                return 
        print("Student record not found.") 
 
    def display_all_students(self): 
        print("All Student Records:") 
        for index, students in enumerate(self.table): 
            for student in students: 
                print(student) 
 
def main(): 
    system = StudentHashTable() 
    while True: 
        print("\nStudent Information System") 
        print("1. Add New Student Record") 
        print("2. Retrieve Student Information by ID") 
        print("3. Delete Student Record by ID") 
        print("4. Display All Student Records") 
        print("5. Exit") 
         
        choice = input("Enter your choice: ") 
        if choice == '1': 
            student_id = int(input("Enter Student ID: ")) 
            name = input("Enter Name: ") 
            age = int(input("Enter Age: ")) 
            major = input("Enter Major: ") 
            student = StudentRecord(student_id, name, age, major) 
            system.add_student(student)         
        elif choice == '2': 
            student_id = int(input("Enter Student ID to retrieve: ")) 
            student = system.retrieve_student(student_id) 
            if student: 
                print("Student Record Found:", student) 
            else: 
                print("Student record not found.")         
        elif choice == '3': 
            student_id = int(input("Enter Student ID to delete: ")) 
            system.delete_student(student_id) 
        elif choice == '4': 
            system.display_all_students() 
        elif choice == '5': 
            print("Exiting the system.") 
            break         
        else: 
            print("Invalid choice, please try again.") 
if __name__ == "__main__": 
 main()