employees = {}
emp_id = 1

def add_employee(name, position, salary):
    global emp_id
    employees[emp_id] = {'name': name, 'position': position, 'salary': salary}
    print(f"Employee {name} added successfully with ID {emp_id}.")
    emp_id += 1

def remove_employee(emp_id):
    if emp_id in employees:
        del employees[emp_id]
        print(f"Employee with ID {emp_id} removed successfully.")
    else:
        print(f"Employee ID {emp_id} not found.")

def display_employees():
    if not employees:
        print("No employees found.")
    else:
        print("ID | Name | Position | Salary")
        print("-----------------------------------")
        for emp_id, details in employees.items():
            print(f"{emp_id} | {details['name']} | {details['position']} | {details['salary']}")

def main():
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. Remove Employee")
        print("3. Display Employees")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter Employee Name: ")
            position = input("Enter Employee Position: ")
            salary = input("Enter Employee Salary: ")
            add_employee(name, position, salary)
        elif choice == "2":
            emp_id_to_remove = int(input("Enter Employee ID to Remove: "))
            remove_employee(emp_id_to_remove)
        elif choice == "3":
            display_employees()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again!")

if __name__ == "__main__":
    main()
