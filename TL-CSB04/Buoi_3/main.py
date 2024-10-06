# Define a class to represent an employee
class Employee:
    def __init__(self, name, age, position, hire_year):
        self.name = name
        self.age = age
        self.position = position
        self.hire_year = hire_year

employees = []

employees.append(Employee("A", 30, "Software Engineer", 2018))
employees.append(Employee("B", 25, "Data Scientist", 2020))

def display_employees():
    for employee in employees:
        print(f"Name: {employee.name}, Age: {employee.age}, Position: {employee.position}, Hire Year: {employee.hire_year}")

display_employees() 

print("="*10)

class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

cars = []

cars.append(Car("Xanh", 30))
cars.append(Car("Đỏ", 20))

def display_car():
    for car in cars:
        print(f"Xe {car.color} chạy được {car.mileage} km")

display_car() 