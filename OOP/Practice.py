# Exercise 1: Create a Class with instance attributes

# Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.
class Vehicle:
    def __init__(self, name, max_speed, capacity):
        self.name = name
        self.max_speed = max_speed
        self.capacity = capacity
    def seating_capacity(self, capacity):
        return f"The capcacity of a {self.name} is {capacity} passengers"
    def fare(self):
        return self.capacity * 100
modelX = Vehicle("Bus", 240, 18)
print(modelX.max_speed, modelX.capacity)

# OOP Exercise 2: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
# Inherite from BUS
class Bus(Vehicle):
    # Assign to default value to capcity
    def seating_capacity(self, capacity = 50):
        return super().seating_capacity(capacity) # Call the func defined in the parent class
School_Bus = Bus("Volvo", 180, 12)
print(School_Bus.seating_capacity())
print(School_Bus.fare())

# In Python, __init__ is what we call a constructor. 
# Its primary job is to initialize a new object's state by assigning values to its properties as soon as the object is created.
# Think of a class as a blueprint and 
# the __init__ method as the assembly line that sets the specific details for each item coming off that blueprint.

class Robot:
    def __init__(self, name, battery_level):
        # This is where we 'set up' the object
        self.name = name
        self.battery_level = battery_level

# Creating two different objects from the same blueprint
bot1 = Robot("R2D2", 100)
bot2 = Robot("C3PO", 45)
#If we were building a game with different characters, we wouldn't want every character to have the same name and health by default.
print(bot1.name) # Output: R2D2
print(bot2.name) # Output: C3PO
#OOP Exercise 1: Create a Class with instance attributes
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    def set_seating_capacity(self, cap):
        self.seating_capacity = cap
    def print_info(self):
        return print(f"This vehicle {self.name} has max speed: {self.max_speed} and mileage: {self.mileage} , number of seat: {self.seating_capacity}")
modelX = Vehicle("modelX",500,200000)

class Bus(Vehicle):
    def seating_capacity(self, bus_capacity):
        super().set_seating_capacity(bus_capacity)
Volvo_Bus = Bus("School Bus", 500, 100000)
Volvo_Bus.seating_capacity(45)
Volvo_Bus.print_info()



