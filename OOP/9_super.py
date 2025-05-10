class User:
    def __init__(self, email):
        self.email = email
    def sign_in(self):
        print("User signed in")
class Wizard(User):
    def __init__(self, name, power, email):
        #User.__init__(self, email) # Call the parent class constructor
        super().__init__(email) # Call the parent class constructor - use supper() to avoid code duplication
        self.name = name
        self.power = power
class Archer(User):
    def __init__(self,name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows
# Example usage
wizard1 = Wizard( "Merlin", 50, "merlin.com")
print(wizard1.email) # User signed in