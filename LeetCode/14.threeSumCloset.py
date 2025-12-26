class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        if len(nums) < 3:
            return 0
        if len(nums) == 3:
            return sum(nums)
        closet = nums[0] + nums[1] + nums[2]
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if abs((nums[i] + nums[j] + nums[k])-target) <= abs(closet-target):
                        closet = nums[i] + nums[j] + nums[k]
        return closet
s = Solution()
print(s.threeSumClosest([-1,2,1,-4], 1))
