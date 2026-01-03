class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        nums.sort()
        min_nums = nums[0]
        result = 0
        if min_nums > 1:
            return 1
        else:
            result = min_nums
            count = 0
            while(count<len(nums)):
                result += 1
                if result > 0 and result not in nums:
                    break
        return result
s = Solution()
print(s.firstMissingPositive([7,8,9,11,12]))
