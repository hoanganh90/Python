def firstUniqueChar(s):
    counts = dict()
    # Remmeber this code is to count a char in a string
    for x in s:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    for x,count in counts.items():
        if count == 1:
            return x
    return None
def firstUniqueChar2(s):
    counts = dict()
    # Remmeber this code is to count a char in a string
    # Ham get() nay la trong counts dict() chu ko fai trong s nhe
    for x in s:
        counts[x] = counts.get(x, 0) + 1
    for x,count in counts.items():
        if count == 1:
            return x
    return None
def firstUniqueNumber(nums):
    counts = dict()
    # Phai nho cai nay, vi no van giu cai order cua array, dung co dung set()
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
    for k,v in counts.items():
        if v == 1:
            return k
    return None

print(firstUniqueChar2("aaaabbcccdee"))
print(firstUniqueNumber([1,2,3,2,2,4,4,5]))
