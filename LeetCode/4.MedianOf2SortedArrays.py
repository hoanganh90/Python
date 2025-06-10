# Given two sorted arrays nums1 and nums2 of size m and n respectively, 
# return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).
from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_nums = nums1 + nums2 # Combine the two arrays
        new_nums.sort()
        length = len(new_nums)
        if length % 2 == 0:
            mid1 = new_nums[length // 2 - 1]
            mid2 = new_nums[length // 2]
            return (mid1 + mid2) / 2
        else:
            return new_nums[length // 2]
# Example usage:
nums1 = [1, 3]
nums2 = [2]
solution = Solution()
result = solution.findMedianSortedArrays(nums1, nums2)
print(result)  # Output: 2.0