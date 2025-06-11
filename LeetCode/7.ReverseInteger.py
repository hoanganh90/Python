# Given a signed 32-bit integer x, return x with its digits reversed. 
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# The [::-1] slice notation in Python is a concise way to reverse a sequence, such as a string or a list.

# Let's break it down:

# The first colon : indicates the start of the slice. When omitted, it defaults to the beginning of the sequence.
# The second colon : indicates the end of the slice. When omitted, it defaults to the end of the sequence.
# The -1 is the step value. A step of -1 means to iterate through the sequence in reverse order, one element at a time.
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
