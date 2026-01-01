def getMoneySpent(keyboards, drives, b):
    totals = []
    for keyboard in keyboards:
        for drive in drives:
            totals.append(keyboard + drive)
    totals.sort()
    result = -1
    if len(totals) == 1:
        return -1 if totals[0] > b else totals[0]
    for i in range(0, len(totals)):
        if totals[i] <= b and totals[i+1] > b:
            result = totals[i]
            break
    return result
print(getMoneySpent([40,50,60],[5,12,8],60))
print(getMoneySpent([4],[5],5))
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        result = -1
        try:
            result = nums.index(target)
        except ValueError:
            result = -1
        return result
s = Solution()
print(s.search([4,5,6,7,0,1,2],3))