class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        lastWord = []
        found_last_char = False
        if i == 0:
            return 1 if s[0] != " " else 0

        while i >= 0:
            if s[i] != " ":
                lastWord.append(s[i])
                if not found_last_char:
                    found_last_char = True
            elif s[i] == " " and found_last_char:
                break
            i -= 1
        return len(lastWord)
s = Solution()
print(s.lengthOfLastWord("a "))
