def multiplication_or_sum(num1, num2):
    # Calulate the product
    product = num1 * num2
    if product > 1000:
        return num1 + num2
    else:
        return product
print(multiplication_or_sum(40,30))
# Ex2 Print the Sum of a Current Number and a Previous number
def Sum_oF_current_and_past(num):
    print("Printing current and previous number and their sum in a range({num})")
    previous_num = 0
    # Loop
    for i in range(1,num):
        x_sum = previous_num + i
        print('Current Number ', i , 'Prevous Number ', previous_num, 'Sum: ', x_sum)
        previous_num = i
print(Sum_oF_current_and_past(10))
