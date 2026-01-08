def countAffordablePairs(prices, budget):
    # Write your code here
    count  = 0
    for i in range(len(prices) - 1):
        for j in range(i + 1, len(prices)):
            if prices[i] + prices[j] <= budget:
                count += 1
    return count
print(countAffordablePairs([1, 2, 3, 4, 5], 7))