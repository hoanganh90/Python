class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
    def __str__(self):
        return f'This toy is {self.color} and is for {self.age} years old.'
action_figures = Toy("red", 0)
print(action_figures.__str__())
print(str(action_figures))
# Dunder methods are special methods that start and end with __ (double underscore)
# They are also called magic methods. They allow us to define the behavior of our objects in Python.
# Dunder methods are used to implement operator overloading, which allows us to define how operators work with our objects.
