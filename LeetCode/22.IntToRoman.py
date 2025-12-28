class Solution:
    def intToRoman(self, num: int) -> str:
        result = ''
        while(True):
            if num >= 1000:
                M_values = num //1000
                for i in range(M_values):
                    result += 'M'
                num = num % 1000
            elif num >= 900 and num < 1000:
                result += 'CM'
                num = num - 900
            elif num >= 500 and num < 900:
                result += 'D'
                num = num - 500
            elif num >= 400 and num < 500:
                result += 'CD'
                num = num - 400
            elif num >= 100 and num < 400:
                C_values = num//100
                for i in range(C_values):
                    result += 'C'
                num = num%100
            elif num >= 90 and num < 100:
                result += 'XC'
                num = num - 90
            elif num >= 50 and num < 90:
                result += 'L'
                num = num - 50
            elif num >=40 and num < 50:
                result += 'XL'
                num = num - 40
            elif num >= 10 and num < 40:
                X_values = num//10
                for i in range(X_values):
                    result += 'X'
                num = num % 10
            elif num == 9:
                result += 'IX'
                num = num - 9
            elif num >= 5 and num <9:
                result += 'V'
                num = num - 5
            elif num == 4:
                result += 'IV'
                num = num - 4
            elif num <4:
                I_values = num//1
                for i in range(I_values):
                    result += 'I'
                num = 0
            if num == 0:
                break
        return result
                
s = Solution()
print(s.intToRoman(4))