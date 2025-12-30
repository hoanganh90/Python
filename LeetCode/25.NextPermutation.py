class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        if len(nums) <= 1:
            return 
        i = len(nums) -1
        while i >= 1:
            if nums[i] > nums[i - 1]:
                j = len(nums) - 1
                while nums[j] <= nums[j-1]:
                    j-=1
                nums[i-1], nums[j] = nums[j], nums[i-1]
                break
            else:
                i -= 1
        nums[i:] = reversed(nums[i:])
s = Solution()
print(s.nextPermutation([2,3,1]))
        