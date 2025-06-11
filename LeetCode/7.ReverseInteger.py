# Given a signed 32-bit integer x, return x with its digits reversed. 
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
class Solution:
    def reverse(self, x: int) -> int:
        output = 0
        if x < 0:
            reversed_x = -int(str(abs(x))[::-1])
        else :
            reversed_x = int(str(x)[::-1])
        if reversed_x < -2**31 or reversed_x > 2**31 - 1:
            return 0
        return reversed_x
# test
solution = Solution()
solution.reverse(0)
