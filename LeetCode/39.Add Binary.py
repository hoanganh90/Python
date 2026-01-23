class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = len(a) if len(a) > len(b) else len(b)
        length_a = len(a)
        length_b = len(b)
        result = []
        extra = 0
        hasExtra = False
        while n > 0:
            if length_a:
                num1 = int(a[length_a-1]) if a[length_a-1].isdigit() else 0
            else:
                num1 = 0
            if length_b:
                num2 = int(b[length_b-1]) if b[length_b-1].isdigit() else 0
            else:
                num2 = 0
            if hasExtra:
                temp = num1 ^ num2  + 1          
            else:
                temp = num1 ^ num2
            result.append(temp)  
            
            hasExtra = num1 and num2    
            n -= 1
            length_a -= 1
            length_b -= 1
            if n == 0 and hasExtra:
                result.append(1)
        return result[::-1]

s = Solution()
print(s.addBinary("11", "1"))
        