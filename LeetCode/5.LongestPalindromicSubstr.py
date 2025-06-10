class Solution:
    def is_palindrome(self, substring: str) -> bool:
        length = len(substring)
        for i in range(length // 2):
            if(substring[i] != substring[length - 1- i]):
                return False
        return True
    def longestPalindrome(self, s: str) -> str:
        left_end = 0
        right_end = len(s) - 1
        longest_palindrome = ""
        while (left_end < len(s)):
            #Detect if a string is a palindrome
            if(self.is_palindrome( s[left_end:right_end + 1])):
                if len(s[left_end:right_end + 1]) > len(longest_palindrome):
                    longest_palindrome = s[left_end:right_end + 1]
                left_end += 1
                right_end = len(s) - 1
            else:
                right_end -= 1
                if(right_end < left_end):
                    left_end += 1
                    right_end = len(s) - 1
        return longest_palindrome if longest_palindrome else ""
# Example usage:
s = "babad"
solution = Solution()
result = solution.longestPalindrome(s)
print(result)  # Output: "bab" or "aba"
            
