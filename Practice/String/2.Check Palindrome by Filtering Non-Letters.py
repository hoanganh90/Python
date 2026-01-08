def extractOnlyLetter(s):
    result = ""
    for x in s:
        if x.isalpha():
            result +=x.lower()
    return result
def isAlphabeticPalindrome(code):
    # Write your code here
    filterString = extractOnlyLetter(code)
    reserverStr = filterString[::-1]
    return True if filterString == reserverStr else False
print(isAlphabeticPalindrome("A1b2B!a"))