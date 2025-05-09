class PlayerCharacters:
    # Public attributes
    # Public attributes are accessible from outside the class
    # Public attributes are not prefixed with an underscore _
    _var_public = "Public" 

    # Private attributes
    # Private attributes are not accessible from outside the class
    # Private attributes are prefixed with two underscores __
    # Class object attributes
    __var_private = "Private"
    memberShip = True # Class attribute - static variable
    def __init__(self, name, age): # Constructor method
        # __ means private, don't try to modify it outside the class
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
    
player1= PlayerCharacters("John", 25)
print(player1._var_public) # Accessing public attribute
#print(player1.__var_private) # Accessing private attribute will raise an error

