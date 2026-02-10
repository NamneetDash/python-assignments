employees = {101: {'name': 'manmaya', 'age': 22, 'department': 'HR', 'salary': 70000}}

def add_employee():
    while True:
        try:
            emp_id = int(input("Enter Employee ID: "))
            if emp_id in employees:
                print("Employee ID already exists. Please enter a unique ID.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a numeric ID.")

    name = input("Enter Name: ")
    try:
        age = int(input("Enter Age: "))
        department = input("Enter Department: ")
        salary = int(input("Enter Salary: "))
        
        employees[emp_id] = {
            'name': name,
            'age': age,
            'department': department,
            'salary': salary
        }
        print("Employee added successfully.")
    except ValueError:
        print("Invalid input for age or salary.")

def view_employees():
    if not employees:
        print("No employees available.")
    else:
        print(f"{'ID':<10} {'Name':<20} {'Age':<10} {'Department':<20} {'Salary':<10}")
        print("-" * 70)
        for emp_id, details in employees.items():
            print(f"{emp_id:<10} {details['name']:<20} {details['age']:<10} {details['department']:<20} {details['salary']:<10}")

def search_employee():
    try:
        emp_id = int(input("Enter Employee ID to search: "))
        if emp_id in employees:
            details = employees[emp_id]
            print("Employee Found:")
            print(f"Name: {details['name']}")
            print(f"Age: {details['age']}")
            print(f"Department: {details['department']}")
            print(f"Salary: {details['salary']}")
        else:
            print("Employee not found.")
    except ValueError:
        print("Invalid input.")

def main_menu():
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search for Employee")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            print("Thank you for using the Employee Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
