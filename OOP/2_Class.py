class PlayerCharacters:
    # Class object attributes
    memberShip = True # Class attribute - static variable
    def __init__(self, name, age): # Constructor method
        self.name = name # Create attribute name
        self.age = age # Create attribute age

    def run(self):
        print(f'run Name: {self.name} Age: {self.age}')
        return "Done"
    def setMemberShip(self, memberShip):
        self.memberShip = memberShip
    def getMemberShip(self):
        return self.memberShip

player1 = PlayerCharacters('John', 50)
print(player1.name) # Output: John
print(player1.run()) # Output: run
print(player1.__getattribute__('name')) # Output: John
print(player1.memberShip) # Output: True

print(player1.setMemberShip(False)) # Output: None()) # Output: True
print(player1.getMemberShip()) # Output: False