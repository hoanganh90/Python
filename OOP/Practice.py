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


