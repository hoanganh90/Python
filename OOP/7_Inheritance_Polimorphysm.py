class User:
    def sign_in(self):
        print("User signed in")
    def attack(self):
        print("Attacking with default power")
class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power
    def attack(self):
        print(f"Attacking with power {self.power}")
class Archer(User):
    def __init__(self,name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows
    def attack(self, tartget):
        print(f"Attacking with arrows: {self.num_arrows} to the target {tartget}")
# Example usage
# Example usage
wizard1 = Wizard( "Merlin", 50)
print(wizard1.sign_in()) # User signed in
wizard1.attack() # Attacking with power 50
archer1 = Archer("Robin", 100)
print(archer1.sign_in()) # User signed in
#archer1.attack() 
archer1.attack("POINT A") # Attacking with arrows: 100 to the target target