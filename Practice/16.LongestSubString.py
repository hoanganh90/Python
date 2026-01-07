def findTheLongestSubString(s):
    result = []
    subStrArray = []
    i = 0
    j = 0
    while i< len(s)-1:
        if s[j] not in subStrArray:
            subStrArray.append(s[j])
            j += 1
        else:
            result.append(len(subStrArray))
            subStrArray = []
            i += 1
            j = i
        if i == len(s):
            break
def findTheLongestSubString2(s):
    char_set = set()
    left = 0
    right = 0
    max_len = 0
    for right in range(len(s)):
        # While we have a duplicate, remove the 1st item on the left
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        # Now adding a new item
        char_set.add(s[right])
        #Calculate the window size: right - left + 1
        max_len =  max(max_len, right - left + 1)
    return max_len
findTheLongestSubString("abcabcbb")
print(findTheLongestSubString2("abcabcbb"))