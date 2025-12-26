class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        foundSign = False
        foundDigit = False
        numberStr = ""
        if s == "":
            return 0
        if s[0].isdigit() == False and (s[0] != " " and s[0] != "+" and s[0] != "-"):
            return 0
        while(True):
            foundLastDigit = False
            if s[i] == " " and len(s) > 1:
                if foundSign:
                    numberStr = "0"
                    break
                else: 
                    foundSign = True
                    i += 1
            if s[i] == "+":
                if foundSign:
                    numberStr = "0"
                    break
                else: 
                    foundSign = True
                    i += 1
            elif s[i] == "-":
                if foundSign:
                    numberStr = "0"
                    break
                else: 
                    foundSign = True
                    numberStr += '-'
                    i += 1
            elif s[i].isdigit():
                    foundDigit = True
                    for j in range(i, len(s)):
                        if s[j].isdigit():
                            numberStr += s[j]
                            if j == len(s) - 1:
                                foundLastDigit = True
                                break
                        else:
                            foundLastDigit = True
                            break
                    i = j+1
            else:
                numberStr = "0"
                break            
            if i >= len(s) or foundLastDigit:
                break
        try:
            convertResult = int(numberStr)
            INT_MAX = 2**31 - 1  #  2147483647
            INT_MIN = -2**31     # -2147483648

            if convertResult > INT_MAX:
                return INT_MAX
            elif convertResult < INT_MIN:
                return INT_MIN
            else:
                return convertResult
            
        except ValueError:
             return 0
    
s = Solution()
result = s.myAtoi(" ")
print(result)