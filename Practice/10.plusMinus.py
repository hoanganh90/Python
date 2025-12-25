def plusMinus(arr):
    countZero = len([ e for e in arr if e == 0])
    countNegative = len([ e for e in arr if e < 0])
    countPositive = len([ e for e in arr if e > 0])
    zeroRatio = countZero/len(arr)
    NegRatio = countNegative/len(arr)
    PositiveRatio = countPositive/len(arr)
    print(f"{PositiveRatio:.6f}\n{NegRatio:.6f}\n{zeroRatio:.6f}")
plusMinus([-4, 3, -9, 0, 4, 1])