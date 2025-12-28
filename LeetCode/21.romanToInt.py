class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        for i in range(len(s)):
            curr = roman[s[i]]
            next_val = roman[s[i+1]] if i+1 < len(s) else 0
            # Neu gia tri hien tai nho hon gia tri tiep theo -> result = result - current
            if curr < next_val:
                result -= curr
            else:
                # Neu gia tri hien tai LON hon gia tri tiep theo -> result = result + current
                result += curr
        return result
s = Solution()
print(s.romanToInt("LIX"))