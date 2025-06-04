"""Biểu diễn các mối quan hệ của các Class"""
# Đây là mối quan hệ Aggregation là vì khi xoá đối tượng Employee -> Thì đối tượng Salary vẫn còn
class Salary():
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus
        
    def calAnnualSalary(self):
        return (self.pay*12)+self.bonus
    
class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    """def __init__(self, name, age, pay, bonus):
        self.name = name
        self.age = age                         => Đây chính là cách code Composition
        self.salary = Salary(pay, bonus)"""
    
    def total_sale(self):
        return self.salary.calAnnualSalary()
    
salary = Salary(10000, 1500)
employee = Employee("Duy", 25, salary)
print(employee.total_sale())
            