import copy
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        result = copy.deepcopy(matrix)
        row_i = 0
        n = len(matrix)
        while row_i < n:
            for j in range(0, n):
                result[j][n - 1 - row_i] = matrix[row_i][j]
            row_i +=1
        # If the goal is to modify the original matrix in-place:
        matrix[:] = result #"Mutates the existing list."
s = Solution()
print(s.rotate([[1,2,3],[4,5,6],[7,8,9]]))
        