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
    @classmethod # Class method - requires cls as the first argument
    def adding_things(cls, a, b):
        return a + b
    @staticmethod # Static method - does not require cls or self
    def adding_things_static(a, b):
        return a + b

