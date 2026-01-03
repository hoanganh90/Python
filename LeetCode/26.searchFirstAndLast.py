class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        results = []
        i = 0
        while i < len(nums):
            if nums[i] == target:
                results.append(i)
            i += 1
        if len(results) == 0:
            return [-1, -1]
        elif len(results) == 1:
            return [results[0], results[0]]
        else:
            return[results[0], results[len(results) - 1]]
s = Solution()
print(s.searchRange([5,7,7,8,8,10], 5))
            
        