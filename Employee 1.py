class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_payroll(self):
        return self.salary

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def calculate_payroll(self):
        return super().calculate_payroll()+ self.bonus

class SalesPerson(Employee):
    def __init__(self, name, salary, comission_rate, sales=0):
        super().__init__(name, salary)
        self.commision_rate = commision_rate
        self.sales = sales

    def calculate_payroll(self):
        return super().calculate_payroll() + (self.sales * self.commision_rate)

name = input('Enter name of Employee: ')
position = input('Enter the position of Employee: ')
salary = int(input('Enter the salary of Employee: '))

if position == "Manager":
    bonus = int(input('Enter bonus of Employee: '))
    employee = Manager(name, salary, bonus)
elif position == "SalesPerson":
    commision_rate = float(input('Enter commision rate of Employee: '))
    sales = int(input('Enter the sales of Employee: '))
    employee = SalesPerson(name, salary, commision_rate, sales)
else:
    employee = Employee(name, salary)

print(f"Payroll for {employee.name}: {employee.calculate_payroll()}")
