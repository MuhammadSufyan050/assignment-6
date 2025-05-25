# 1. Using self

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Marks: {self.marks}")

student_1 = Student("Ahmed",91)
student_1.display()

print("--------------------------------")

# 2. Using cls
class Counter:
    count = 0
    def __init__(self):
        Counter.count += 1

    @classmethod
    def display_counter(cls):
        print(f"My total created objects are: {cls.count}")

obj_1 = Counter()
obj_2 = Counter()
obj_3 = Counter()
obj_4 = Counter()

Counter.display_counter()

print("--------------------------------")


# 3. Public Variables and Methods

class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} is starting...!")

my_car = Car("BMW")
print(my_car.brand)
my_car.start()

print("--------------------------------")

# 4. Class Variables and Class Methods

class Bank:
    bank_name = "Bank AL Habib"

    def __init__(self, account_holder):
        self.account_holder = account_holder

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def display(self):
        print(f"Account Holder: {self.account_holder}, Bank: {self.bank_name}")

account_1 = Bank("Abdul Rafey")
account_2 = Bank("Hasnain")

account_1.display()
account_2.display()

Bank.change_bank_name("Meezan Bank")

account_1.display()
account_2.display()

print("--------------------------------")

# 5. Static Variables and Static Methods

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
    
result = MathUtils.add(67,33)
print("Sum of my 2 numbers are: ", result)

print("--------------------------------")

# 6. Constructors and Destructors

class Logger:
    def __init__(self):
        print("Message before: Logger object created.")

    def __del__(self):
        print("Message after: Logger object destructor.")

log = Logger()
del log

print("--------------------------------")

# 7. Access Modifiers: Public, Private, and Protected

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name 
        self._salary = salary           
        self.__ssn = ssn                

    def set_salary(self, new_salary):
        if new_salary > 0:
            self._salary = new_salary
        else: 
            print("Salary must be a positive number")

    def get_ssn(self):
        return self.__ssn

    def display(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self._salary}")
        print(f"SSN: {self.__ssn}")

class Manager(Employee):
    def __init__(self, name, salary, ssn, department):
        super().__init__(name, salary, ssn)
        self.department = department

    def show_manager_info(self):
        print(f"Manager: {self.name}")
        print(f"Department: {self.department}")
        print(f"Protected Salary: {self._salary}")
        print(f"Accessing SSN via getter: {self.get_ssn()}")


m = Manager("Ali", 12000, "222-525-3090", "Information Technology")


m.show_manager_info()

m.set_salary(35000)
print("Updated Salary:", m._salary)

print("Private SSN via name mangling:", m._Employee__ssn)  

print("--------------------------------")

# 8. The super() Function

class Person:
    def __init__(self, name):
        self.name = name
        print(f"Person created with the name: {self.name}")

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
        print(f"Teacher teaches: {self.subject}")

t = Teacher("Arif Rozani", "GIAIC Artificial Intelligence")

print("--------------------------------")

# 9. Abstract Classes and Methods

from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
rect = Rectangle(2,6)
print("Area of the Rectuangle", rect.area())

print("--------------------------------")

# 10. Instance Methods

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says: Woof Woof")

dog1 = Dog("Buddy", "Aidi")
dog1.bark()