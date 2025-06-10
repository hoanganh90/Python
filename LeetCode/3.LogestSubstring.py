# Given a string s, find the length of the longest substring without duplicate characters.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        list_lengths = []
        current_substring = ""
        index = 0
        if len(s) == 1:
            return 1
        while True:
            for char in s[index:]:
                if(char not in current_substring):
                    current_substring += char
                else:
                    list_lengths.append(len(current_substring))
                    current_substring = "" # Reset current_substring
                    break   
            index += 1
            if index >= len(s):
                break
        return max(list_lengths) if list_lengths else 0
    
# Example usage:
s = "ohomm"
solution = Solution()
result = solution.lengthOfLongestSubstring(s)
print(result)  # Output: 3
