class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix)
        c = len(matrix[0]) - 1
        cols = len(matrix[0])
        row = 0
        for i in range(r):
            if (i == 0 and target <= matrix[0][c]):
                break
            if (target <= matrix[i][c] and target > matrix[i-1][c]):
                row = i
                break
        for j in range(cols):
            if (matrix[row][j] == target):
                return True
        return False


        