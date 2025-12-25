def BracketCombinations(num):
    if num == 0:
        return 1
    catalan = [0] * (num + 1)
    catalan[0] = 1
    for i in range(1, num + 1):
        for k in range(i):
            catalan[i] += catalan[k] * catalan[i - 1 - k]
    return catalan[num]
# Cn = (k = 0 to n - 1) ∑ Ck × Cn−1−k
# keep this function call here 
print(BracketCombinations(4))