import utility as util # We can import a module as it is a file
import Packages.Shopping.shoppingCart as cart # We cannot import a module as it is in a folder
# We can import a module by defining the path to the module with a dot (.)
print(util.add(5, 10))
print(util.subtract(10, 5))
print(util.multiply(5, 10))
print(util.divide(10, 5))
cart.buy("apple")