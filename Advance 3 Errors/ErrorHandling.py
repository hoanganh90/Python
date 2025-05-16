# Error Handling
# Error handling is a way to respond to errors that occur in your program.
# It allows you to gracefully handle errors and continue executing your program.
# In Python, you can use try and except blocks to handle errors.
def hello():
    try:
        # This will raise a NameError because 'name' is not defined
        print(f"Hello, {name}!")
    except NameError as e:
        # This block will execute if a NameError occurs
        print(f"An error occurred: {e}")
    finally:
        # This block will always
        print("This will always execute")

hello()

age = input('Whaat is your age?: ')
try: 
    age = int(age)
    print(f'Your age is {age}')
except ValueError:
    print('Please enter a real number')
else:
    print('No errors occurred')
finally:
    print('Thank you!')