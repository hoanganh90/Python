class Solution:
    def jump(self, nums: list[int]) -> int:
        near = far = jumps = 0
        while far < len(nums) - 1:
            farthest = 0
            for i in range(near,far + 1):
                farthest = max(farthest, i + nums[i])
            near = far +1
            far = farthest
            jumps += 1
        return jumps
s = Solution()
print(s.jump([2,3,0,1,4]))