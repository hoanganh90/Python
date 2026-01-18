class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = sum(nums)
        window_size = 1
        n = len(nums)
        while window_size < n:
            for i in range(n - window_size+1):
                tmp_sum = sum(nums[i:i+window_size])
                max_sum = max(tmp_sum, max_sum)
            window_size += 1
        return max_sum
    def maxSubArray2(self, nums: list[int]) -> int:
        max_so_far = nums[0]
        current_running_sum = 0
        for x in nums:
            # If current_running_sum is negative, throw it away and start at x
            current_running_sum = max(x, current_running_sum + x)
            # Keep track of the best sum we've ever seen
            max_so_far = max(max_so_far, current_running_sum)
        return max_so_far
s = Solution()
print(s.maxSubArray2([-2,1,-3,4,-1,2,1,-5,4]))

            