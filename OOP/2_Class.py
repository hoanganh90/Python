class PlayerCharacters:
    # Class object attributes
    memberShip = True # Class attribute
    def __init__(self, name, age):
        self.name = name # Create attribute name
        self.age = age # Create attribute age

    def run(self):
        print(f'run Name: {self.name} Age: {self.age}')

player1 = PlayerCharacters('John', 50)
print(player1.name) # Output: John
print(player1.run()) # Output: run
print(player1.__getattribute__('name')) # Output: John
print(player1.memberShip) # Output: True