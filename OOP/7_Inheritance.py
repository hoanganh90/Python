class User:
    def sign_in(self):
        print("User signed in")
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
    def attack(self):
        print(f"Attacking with arrows: {self.num_arrows} left")
# Example usage
wizard1 = Wizard( "Merlin", 50)
print(wizard1.sign_in()) # User signed in
wizard1.attack() # Attacking with power 50
archer1 = Archer("Robin", 100)
print(archer1.sign_in()) # User signed in
archer1.attack() 