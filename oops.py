# Q1. Create a class Person with attributes
# name and age, and a method display() to print
# them. Create a class Employee that inherits from Person and adds an attribute salary with a method
# to display all details.
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f"Name:{self.name}")
        print(f"Age:{self.age}")
class employee(person):
    def __init__(self,name,age,salary):
        super().__init__(name,age)
        self.salary=salary
    def display(self):
        super().display()
        print(f"Salary:{self.salary}")
e1 = employee("Saima Akabr",28,90000)
e1.display()

# Q2. Create a class Vehicle with a method fuel_type() that prints
# "Uses petrol/diesel". Create a class Car that inherits
# from Vehicle, adds a method num_wheels() that prints "4 wheels", and calls both methods from an object of Car.

class vehicle:
    def fuel_type(self):
        print("Uses petrol/diesel")
class Car(vehicle):
    def num_wheels(self):
        print("4 wheels")
        
c1=Car()
c1.fuel_type()
c1.num_wheels()

# wap to create a student class and dispaly student details

# class and object
class student:
    def display(self):
        print("my name is saima ")
        print("i am student")
s1= student()
s1.display()

#2 constructor(__init__)
# wap to display a student's name and age
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
        
    def display(self):
        print(self.name)
        print(self.age)

s1=student("saima",23)
s1.display()
# inheritance    
#wap in which child class uses the parent class method
class parent:
    def show(self):
        print("this is parent class ")
        
class child(parent):
    def display(self):
        print("this is child class")
        
obj = child()
obj.show()
obj.display()

# Write a Python program to create a Student class that stores a student's name and prints it.
        
class student:
    def __init__(self,name):
        self.name=name
        
    def display(self):
        print(self.name)
        
s1=student("saima")
s1.display()
    
# ...
# Write a Python program where:
# - The Parent class has a show() method that prints "This is parent".
# - The Child class inherits from Parent and has a display() method that prints "This is child".
# - Create a child object and call both methods.   
# ...    
#     
class parent:
    def show(self):
        print("this parent")
        
class child(parent):
    def display(self):
       print("this is child")
       
obj = child()
obj.show()
obj.display()

# — Encapsulation 
# Now let's practise another important OOPS concept.
# Write a Python program to create a Bank class with a private variable __balance = 5000 and a
# show_balance() method to print the balance.

class bank :
    def __init__(self,balance):
        self.__balance=balance
        
    def show_balance(self):
         print(self.__balance)
         
bal = bank(50000)
bal.show_balance()
       
        
        
        