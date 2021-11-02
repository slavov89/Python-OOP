class Employee:
    def __init__(self, ide,first_name: str, last_name: str, salary):
        self.id = ide
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_annual_salary(self):
        return int(self.salary*12)

    def raise_salary(self, amount: int):
        self.salary += amount
        return self.salary


employee = Employee(744423129, "John", "Smith", 1000)
print(employee.get_full_name())
print(employee.raise_salary(500))
print(employee.get_annual_salary())
 