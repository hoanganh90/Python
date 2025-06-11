class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x == 0:
            return True 
        elif x < -2**31 or x > 2**31 -1:
            return False
        else:
            temp = x
            x = int(str(x)[::-1])
            return temp == x
# Sample test
solution = Solution()
print(solution.isPalindrome(121))