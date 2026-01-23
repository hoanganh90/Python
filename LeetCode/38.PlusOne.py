class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        result = []
        n = len(digits) - 1
        extra = 0
        isLastItem = True
        if n == 0:
            temp = (digits[n] + 1) % 10
            result.append(temp)
            extra = (digits[n] + 1) // 10
            if extra > 0:
                result.append(extra)
        while n > 0:
            if isLastItem:
                temp = (digits[n] + 1) % 10
                extra = (digits[n] + 1) // 10
                result.append(temp)
                isLastItem = False
            n -= 1
            if extra > 0:
                temp = (digits[n] + extra) % 10
                extra = (digits[n] + extra) // 10
            else:
                temp = digits[n] % 10
            result.append(temp)
            if n == 0:
                if extra > 0:
                    result.append(extra)
        return result[::-1]
s = Solution()
print(s.plusOne([9]))
