def runLengthCoding(s):
    counts = dict()
    for x in s:
        counts[x] = counts.get(x, 0) + 1
    result = ""
    for k,v in counts.items():
        result += str(v) + str(k)
    return result
print(runLengthCoding("aaaabbaabbcccc"))