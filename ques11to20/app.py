
# 11. Class Methods

class Book: 
    total_books = 0

    @classmethod
    def increment_book_count(cls):
         cls.total_books += 1

Book.increment_book_count()
Book.increment_book_count()
Book.increment_book_count()
Book.increment_book_count()
Book.increment_book_count()
Book.increment_book_count()


print(Book.total_books)

print("--------------------------------")

# 12. Static Methods

class TemperatureConverter:

    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) +32
    
print(TemperatureConverter.celsius_to_fahrenheit(29))

print("--------------------------------")

# 13. Composition

class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self, engine):
        self.engine = engine

    def start_car(self):
        self.engine.start()

e = Engine()
c =Car(e)
c.start_car()

print("--------------------------------")

# 14. Aggregation

class Employee:
    
    def __init__(self, name):
        self.name = name 

class Department:
    def __init__(self, employee):
        self.employee = employee
    
emp = Employee("Abdullah")

dep = Department(emp)
print(dep.employee.name)

print("--------------------------------")

# 15. Method Resolution Order (MRO) and Diamond Inheritance

class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass

d =D()

print(D.__mro__)

print("--------------------------------")

# 16. Function Decorators

def log_function_call(func):
    def wrapper():
        print("Function is being called")
        return func()
    return wrapper

@log_function_call
def say_hello():
    print("Hello, Hasnain")

say_hello()

print("--------------------------------")

# 17. Class Decorators

def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    
    cls.greet = greet
    return cls

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name 

    def introduce(self):
        return f"Hi, I'm {self.name}"
    
per = Person("Ahmed")
print(per.greet())

print("--------------------------------")

# 18. Property Decorators: @property, @setter, and @deleter

class Product:
    def __init__(self, name, price):
        self.name = name 
        self._price = price
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if value < 0:
            print("Price cannot be negative!") 
        else:
            self._price = value
    
    @price.deleter
    def price(self):
        print(f"Deleting the price of {self.name}")
        del self._price

product = Product("Bike", 45000)

print(product.price)

product.price = 52000
print(product.price)

product.price = -500

del product.price

print("--------------------------------")

# 19. callable() and __call__()

class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, number):
        return number * self.factor
    
multi = Multiplier(8)
print(callable(multi))

result = Multiplier(12)
print(result)

print("--------------------------------")

# 20. Creating a Custom Exception

class InvalidAgeError(Exception):
    def __init__(self, message = "Age must be 18 or older"):
        self.message = message
        super().__init__(self.message)

def check_age(age):
    if age < 18:
        raise InvalidAgeError(f"Invalid age: {age}. You must be 18 or older.")
    else:
        print(f"Age {age} is valid!")

try:
    age = int(input("Enter your age: "))
    check_age(age)
except InvalidAgeError as e:
    print(f"Error: {e}")
except ValueError:
    print("Please enter a valid integer for age.")