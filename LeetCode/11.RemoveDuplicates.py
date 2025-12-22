class Solution:
    def removeDuplicates(self, nums: list[int]) -> any:
        set_nums = set(nums)
        result = []
        for i in range(len(nums)):
            if nums[i] in set_nums and nums[i] not in result:
                result.append(nums[i])
        return len(set_nums)
    def removeDuplicates3(self, nums: list[int]) -> int:
        if not nums:
            return 0
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1  
        print(nums)
        return k
s = Solution()
print(s.removeDuplicates3([0,0,1,1,1,2,2,3,3,4]))