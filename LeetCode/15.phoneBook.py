class Solution:
    def getCharFromAsciiByN(self, N):
        match N:
            case "2":
                return ['a','b','c']
            case "3":
                return ['d','e','f']
            case "4":
                return ['g','h','i']
            case "5":
                return ['j','k','l']
            case "6":
                return ['m','n','o']
            case "7":
                return ['p','q','r', 's']
            case "8":
                return ['t','u','v']
            case "9":
                return ['w','x','y', 'z']
    def letterPairCombinations(self, digits: str) -> list[str]:
        if len(digits) == 1:
            return self.getCharFromAsciiByN(digits[0])
        else:
            matrix_letters = []
            for i in digits:
                matrix_letters.append(self.getCharFromAsciiByN(i))
            #print(matrix_letters)
            count_row = 0
            result = []
            temp_matrix = matrix_letters
            while(True):
                count_row = len(temp_matrix)
                if len(temp_matrix) == 0:
                    break
                elif len(temp_matrix) > 0:
                    first_row = temp_matrix[0]
                    for i in range(1, len(temp_matrix)):
                        next_row = temp_matrix[i]
                        for j in first_row:
                            for k in next_row:
                                result.append(j+k)
                    count_row -=1
                if count_row > 0:
                    temp_matrix.pop(0)
                else: break
            return result
# test
s = Solution()
print(s.letterPairCombinations("29"))      