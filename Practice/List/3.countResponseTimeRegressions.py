def countResponseTimeRegressions(responseTimes):
    if responseTimes == 0 or len(responseTimes) == 0:
        return 0
    count = 0
    i = 1
    sum = responseTimes[0]
    avarage  = responseTimes[0]
    while i < len(responseTimes):
       
        sum += responseTimes[i]
        avarage = sum // (i+1)
        if responseTimes[i] > avarage:
            count += 1
        i += 1
    return count
# O(N)
print(countResponseTimeRegressions(0))