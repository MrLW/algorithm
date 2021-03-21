from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        常量解决方案
        """
        cols, rows = set(), set()
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if(matrix[row][col] == 0):
                    cols.add(col)
                    rows.add(row)
        for row in rows:
            for i in range(len(matrix[0])):
                matrix[row][i] = 0
        for col in cols:
            for i in range(len(matrix)):
                matrix[i][col] = 0
        return matrix
s = Solution()
matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
s.setZeroes(matrix)
print(matrix)
