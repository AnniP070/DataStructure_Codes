class Patient: 
    def __init__(self, patient_nm, disease, priority): 
        self.patient_nm = patient_nm 
        self.disease = disease 
        self.priority = priority 
        self.next = None 
 
class HospitalManagement: 
    def __init__(self): 
        self.head = None 
 
    def create_patient(self, patient_nm, disease, priority): 
        return Patient(patient_nm, disease, priority) 
 
    def add_patient(self, patient_nm, disease, priority): 
        new_node = self.create_patient(patient_nm, disease, priority) 
         
        if self.head is None: 
            self.head = new_node 
        else: 
            current = self.head 
            while current.next: 
                current = current.next 
            current.next = new_node 
 
    def remove_patient(self): 
        if self.head is None: 
            print("Queue is empty") 
            return 
         
        # To remove head node 
        removed_patient = self.head 
        self.head = self.head.next 
        print(f"Removed patient: {removed_patient.patient_nm}") 
        del removed_patient 
 
    def print_list(self): 
        current = self.head 
        while current: 
            print(f"Patient Name: {current.patient_nm}, Disease: {current.disease}, Priority: {current.priority}") 
            current = current.next 
        if not self.head: 
            print("Queue is empty") 
 
    def search_patient(self, patient_nm): 
        current = self.head 
        while current: 
            if current.patient_nm == patient_nm: 
                print(f"Patient found: Name: {current.patient_nm}, Disease: {current.disease}, Priority: {current.priority}") 
                return 
            current = current.next 
        print("Patient not found") 
 
    def move_high_priority(self, patient_nm): 
        current = self.head 
        previous = None 
        found_patient = None 
 
        # First, find the patient and detach them from the current position 
        while current: 
            if current.patient_nm == patient_nm: 
                found_patient = current 
                # If patient is not already at the front 
                if previous: 
                    previous.next = current.next 
                else: 
                    # If patient is already at the head, just update priority and skip rearranging 
                    found_patient.priority = 1 
                    print(f"Patient {found_patient.patient_nm} already has highest priority.") 
                    return 
                break 
            previous = current 
            current = current.next 
         
        if found_patient: 
            # Move patient to the front (highest priority) 
            found_patient.next = self.head 
            self.head = found_patient 
            self.head.priority = 1  # Assign highest priority to this patient 
             
            # Update the priorities of all other patients 
            current = self.head.next 
            priority_counter = 2 
            while current: 
                current.priority = priority_counter 
                priority_counter += 1 
                current = current.next 
             
            print(f"Moved patient {found_patient.patient_nm} to highest priority.") 
        else: 
            print("Patient not found") 
 
    def update_patient_info(self, patient_nm): 
        current = self.head 
        while current: 
            if current.patient_nm == patient_nm: 
                print(f"Current info - Name: {current.patient_nm}, Disease: {current.disease}, Priority: {current.priority}") 
                current.disease = input("Enter new Disease: ") 
                current.priority = int(input("Enter new Priority: ")) 
                print(f"Updated info - Name: {current.patient_nm}, Disease: {current.disease}, Priority: {current.priority}") 
                return 
            current = current.next 
        print("Patient not found")    
 
# Main Menu 
ll = HospitalManagement() 
 
ll.add_patient("Shreaysh","Fever",1) 
ll.add_patient("Varad","Cold",2) 
ll.add_patient("Arpita","Headache",3) 
 
while True: 
    print("\n1. To add new Patient (at end of queue)") 
    print("2. To remove Patient who has been Treated") 
    print("3. Move above Priority (Emergency Case)") 
    print("4. Display current queue") 
    print("5. Search specific Patient") 
    print("6. Update patient info") 
    print("7. Exit") 
    term = int(input("Enter Your Choice: ")) 
 
    if term == 1: 
        patient_nm = input("Enter Patient Name: ") 
        disease = input("Enter Disease: ") 
        priority = int(input("Enter Priority: ")) 
        ll.add_patient(patient_nm, disease, priority) 
    elif term == 2: 
        ll.remove_patient() 
    elif term == 3: 
        patient_nm = input("Enter Patient Name to move to top priority: ") 
        ll.move_high_priority(patient_nm) 
    elif term == 4: 
        print("Current Queue:") 
        ll.print_list() 
    elif term == 5: 
        patient_nm = input("Enter Patient Name to search: ") 
        ll.search_patient(patient_nm) 
    elif term == 6: 
        patient_nm = input("Enter Patient Name to update: ") 
        ll.update_patient_info(patient_nm) 
    elif term == 7: 
        print("Exiting") 
        break 
    else: 
        print("Invalid Choice")