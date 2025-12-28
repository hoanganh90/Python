class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if abs(divisor) > abs(dividend):
            return 0
        result = 1
        temp_divisor = divisor
        while(True):
            temp_divisor += divisor 
            if abs(temp_divisor) < abs(dividend):
                result += 1
            else: break
        return result if (divisor < 0) == (dividend < 0) else 0 - result
s = Solution()
print(s.divide(-7,-2))
        
        