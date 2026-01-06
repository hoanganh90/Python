class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        if len(nums) == 1:
            return [nums]
        if len(nums) == 2:
            return [nums, nums[-1::-1]]
        i = 0
        result = [nums.copy()]
        shift_count = len(nums)
        count = 0
        nums_copy = nums.copy()
        while True:
            for j in range(i + 1, len(nums) - 1):
                for t in range (j + 1, len(nums)):
                    nums_copy[j], nums_copy[t] = nums_copy[t], nums_copy[j]
                    result.append(nums_copy[:])
            count += 1
            if count == shift_count:
                break
            elif count < len(nums):
                first_element = nums[0]
                nums.pop(0)
                nums.append(first_element)
                nums_copy = nums.copy()
                result.append(nums_copy[:])
                i = 0 # Reset i
        return result
s = Solution()
print(s.permute([5,4,6,2]))
print(len(s.permute([5,4,6,2])))
        