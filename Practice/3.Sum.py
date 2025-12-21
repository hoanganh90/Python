class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        output = []
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums),1):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = [nums[i], nums[j], nums[k]]
                        if triplet not in output:
                            output.append(triplet)
        return output
test = Solution()
test.threeSum([-1,0,1,2,-1,-4])
print(test.threeSum([-1,0,1,2,-1,-4]))
        