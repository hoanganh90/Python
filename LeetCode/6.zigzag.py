class Solution:
    def convert(self, s: str, numRows: int) -> str:
        result = ""
        # Calculate the length of str
        length = len(s)
        if numRows <= 1 or length <= 1:
            return s
        # Calulate the number of columns
        numCols = length//(numRows + numRows - 2)
        if numCols == 0:
            return s
        extra = length % (numRows + numRows - 2)
        if extra == 0 and numCols == 1:
            extra = numRows
        if extra < numRows:
            numCols = int(numCols)*(numRows - 1) + 1
        else:
            numCols = int(numCols)*(numRows - 1) + extra - numRows
        # Create a 2D array to hold the zigzag pattern
        zigzag = [["" for _ in range(numCols)] for _ in range(numRows)]
        rowValue = 0
        colValue = 0
        direction = 0
        loop = 0
        while True:
            if rowValue < numRows:  # Print in column
                zigzag[rowValue][colValue] = s[direction]
                rowValue += 1
                direction += 1
                row_diag = numRows - 2
                col_diag = colValue + 1
            if rowValue == numRows:   # Print in diagal
                zigzag[row_diag][col_diag] = s[direction]
                direction += 1
                row_diag -= 1
                col_diag += 1
                if row_diag == 0:
                    loop +=1
                    colValue = loop * (numRows - 1)
                    rowValue = 0
            if direction >= length:
                break
        for i in range(numRows):
            for j in range(numCols):
                if(zigzag[i][j] != ""):
                    result += zigzag[i][j]
        return result
# Example
s = "AB"
numRows = 2
solution = Solution()
result = solution.convert(s, numRows)
print(result)  # Output