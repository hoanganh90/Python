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
s = Solution()
print(s.maxSubArray([-2,1]))

            