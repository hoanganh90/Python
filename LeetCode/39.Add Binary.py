class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = len(a) if len(a) > len(b) else len(b)
        length_a = len(a)
        length_b = len(b)
        result = []
        extra = 0
        hasExtra = False
        while n > 0:
            if length_a > 0:
                num1 = int(a[length_a-1]) if a[length_a-1].isdigit() else 0
            else:
                num1 = 0
            if length_b > 0:
                num2 = int(b[length_b-1]) if b[length_b-1].isdigit() else 0
            else:
                num2 = 0
            if hasExtra:
                tmp = num1 + num2 + extra
            else:
                tmp = num1 + num2
            if tmp > 1:
                hasExtra = True
                extra = 1
                result.append(tmp % 2)
            else:
                result.append(tmp)
                
            n -= 1
            length_a -= 1
            length_b -= 1
            if n == 0 and hasExtra:
                result.append(1)
            str_result = "".join(map(str,result[::-1]))
        return str_result

s = Solution()
print(s.addBinary("1010", "1011"))
        