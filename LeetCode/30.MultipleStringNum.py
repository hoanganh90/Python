class Solution:
    def convertStr2Num(self, numStr):
        n = len(numStr)
        result = 0
        i = 0
        while i < len(numStr) > 0:
            result += (ord(numStr[i]) - 48 ) * 10 ** (len(numStr) - i - 1)
            i += 1
        return result
    def multiply(self, num1: str, num2: str) -> str:
        return str(self.convertStr2Num(num1) * self.convertStr2Num(num2))
s = Solution()
print(s.multiply("123", "456"))