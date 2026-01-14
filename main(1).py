class Employee:
    """Common base class for all employees"""
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tasks = {}
        Employee.empCount += 1

    def display_emp_count(self):
        "Displays the number of employees"
        print(f"Total number of employee(s) is {Employee.empCount}")

    def display_employee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

    def __del__ (self):
        Employee.empCount -=1

    def update_salary(self, new_salary):
        self.salary = new_salary

    def modify_task(self, task_name, status="New"):
        self.tasks[task_name]=status

    def display_task(self, status):
        print(f"Taskuri cu statusul {status}")
        for name in self.tasks.keys():
            if self.tasks[name] == status:
                print(name)

class Manager(Employee):
    mgr_count = 0

    def __init__(self, name, salary, tasks, department):
        super().__init__(name, salary)
        self.tasks = tasks
        self.department = "EchipaMea_" + department
        Manager.mgr_count += 1

    def display_employee(self):
        print(f"Task-urile managerului {self.name}: {list(self.tasks.keys())}")

if __name__ == "__main__":
    X = 15
    Y = 7
    
    print(f"Configuratie: X={X} (Rest 3 -> Afisare Taskuri), Y={Y} (Creare {int(Y/3)} manageri)\n")

    lista_manageri = []

    m1 = Manager(
        name="Andrei Manager", 
        salary=6000, 
        tasks={"Raport_Q1": "Done", "Planificare_Q2": "In Progress"}, 
        department="Vanzari"
    )
    lista_manageri.append(m1)

    m2 = Manager(
        name="Ioana Manager", 
        salary=7000, 
        tasks={"Audit_Intern": "Pending", "Recrutare": "In Progress"}, 
        department="HR"
    )
    lista_manageri.append(m2)

    emp1 = Employee("Marcel Angajat", 3500)

    print("--- Rezultate metoda display_employee ---")
    
    print("\n[Pentru Manageri]:")
    for mgr in lista_manageri:
        mgr.display_employee()

    print("\n[Pentru Employee standard]:")
    emp1.display_employee()

    print("\n--- Verificare Contoare ---")
    print(f"Total angajați (prin instanța emp1): {emp1.empCount}")
    
    print(f"Total angajați (prin instanța m1): {m1.empCount}")
    
    print(f"Total Manageri (variabila de clasa mgr_count): {Manager.mgr_count}")