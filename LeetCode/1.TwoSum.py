from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        result = []
        while True:
            if i >= len(nums) - 1: 
                break
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    result.append(i)
                    result.append(j)
                    break
            i+= 1       
        return result
# Example usage
solution = Solution()
nums = [2, 7, 11, 15]
target = 9
result = solution.twoSum(nums, target)
print(result)  # Output: [0, 1] since nums[0] + nums[1] == 9