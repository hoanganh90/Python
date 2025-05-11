class User:
    def __init__(self, email):
        self.email = email
    def sign_in(self):
        print("User signed in")
class Wizard(User):
    def __init__(self, name, power, email):
         self.name = name
         self.power = power
         self.email = email
       
class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows
    def run(self):
        print("Archer Run")

class HybridBorg(Wizard, Archer): # Hybrid inheritance - multiple inheritance - The ORDER is important
# In Python, the order of inheritance matters. The first class in the list is the one that will be used to resolve any conflicts.
# In this case, if both Wizard and Archer have a method with the same name, the method from Wizard will be used.
# This is because Wizard is the first class in the list of classes that HybridBorg inherits from.
    def __init__(self, name, power, email, num_arrows):
        Archer.__init__(self, name, num_arrows) # Call the Archer class constructor
        Wizard.__init__(self, name, power, email) # Call the parent class constructor
# Example usage
wizard1 = Wizard( "Merlin", 50, "merlin.com")
print(wizard1.email) # User signed in
# Introspection
print(dir(wizard1)) # <class '__main__.Wizard'>

# Example usage of HybridBorg
hybrid = HybridBorg("Borg", 100, "borg.com", 50)
print(hybrid.name) # Borg
print(hybrid.power) # 100
print(hybrid.email) # borg.com
print(hybrid.num_arrows) # 50
print(hybrid.run()) # Run