def do_stuff(num):
    try:
        num = int(num)  # Ensure the input is an integer
        return num + 5
    except ValueError:
        raise ValueError("Input must be an integer")
    
if __name__ == "__main__":
    test_num = 10
    result = do_stuff(test_num)
    print(f"Result for input {test_num}: {result}")  # This will print the result of the function call
    # You can add more test cases here if needed