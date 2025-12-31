def bonAppetit(bill, k, b):
    # Write your code here
    sum = 0
    for i in range(0, len(bill)):
        if i != k:
            sum += bill[i]
    average = sum / 2
    if b - average == 0:
        return print("Bon Appetit")
    else:
        return print(int(b - average))
print(bonAppetit([3,10,2,9], 1, 12))

                