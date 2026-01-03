class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        result = -1
        for i in range(0, len(nums)):
            if i == 0 and nums[i] > target:
                result = 0
                break
            if i == len(nums) - 1 and nums[i] < target:
                result = len(nums)
                break
            if nums[i] == target:
                result = i
                break
            if nums[i] < target and nums[i+1] > target:
                result = i + 1
                break
        return result
s = Solution()
print(s.searchInsert([1,3,5,6], 5))

            
