class Employee:
    def __init__(self, name,employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        print(f"\nEmployee Details:")
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary:$ {self.salary:,.2f}")

    def update_salary(self,new_salary):
        self.salary = new_salary
        return f"New salary is ${new_salary:,.2f}"

class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        return f"Employee {employee.name} added to {self.department_name}"

    def total_salary_expenditure(self):
        total=sum(emp.salary for emp in self.employees)
        print(f"\nTotal Salary Expenditure: {total:,.2f}")
        return total

    def display_all_employees(self):
        if not self.employees:
            print("No employees added to this department yet")
            return
        print(f"\nEmployees in {self.department_name}:")
        for i, emp in enumerate(self.employees,1):
            print(f"{i}. {emp.name} (ID: {emp.employee_id})-$ {emp.salary:,.2f}")

if __name__ == "__main__":
    dept_name=input("Enter department name: ")
    department=Department(dept_name)

    while True:
        print("\nEmployee Mananagement system")
        print("1. Add Employee")
        print("2.Update salary")
        print("3.View department salary expenditure")
        print("4.List all employees")
        print("5.Exit")

        choice=input("Enter your choice: ")

        if choice=="1":
            name=input("Enter employee name: ")
            emp_id=input("Enter employee ID: ")

            try:
                salary=float(input("Enter salary: "))
                new_emp=Employee(name, emp_id, salary)
                print(department.add_employee(new_emp))
            except ValueError:
                print("Invalid input")

        elif choice=="2":
            if not department.employees:
                print("No employees added to this department yet")
                continue

            department.display_all_employees()
            try:
                emp_choice=int(input("Enter employee choice: "))-1
                selected_emp=department.employees[emp_choice]
                print(selected_emp.display_details())
            except (ValueError, IndexError):
                print("Invalid input")

        elif choice=="3":
            department.total_salary_expenditure()

        elif choice=="4":
            department.display_all_employees()

        elif choice=="5":
            print("Goodbye")
            break

        else:
            print("Invalid input.Pick a number between 1 and 5")




