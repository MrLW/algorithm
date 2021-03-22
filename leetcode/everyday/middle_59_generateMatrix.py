from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        '''
        螺旋矩阵 II: 给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 
        思路: 循环的方式, 依次给 i*i的正方形的上边、右边、下边、左边设置值, 
        '''
        ret = [[0 for i in range(n)] for j in range(n)]
        startRow, endRow, startCol, endCol, x = 0, n, 0, n, 0
        while startCol < endCol and startRow < endRow:
            # 上边: 从左-->右
            for col in range(startCol, endCol):
                x += 1
                ret[startRow][col] = x
            startRow += 1
            # 右边: 从上-->下
            for row in range(startRow, endRow):
                x += 1
                ret[row][endCol-1] = x
            endCol -= 1
            # 下边: 从右-->左
            for col in reversed(range(startCol, endCol)):
                x += 1
                ret[endRow-1][col] = x
            endRow -= 1
            # 左边: 从下-->上
            for row in reversed(range(startRow, endRow)):
                x += 1
                ret[row][startCol] = x
            startCol += 1
        return ret


s = Solution()
n = 4
print('螺旋矩阵', s.generateMatrix(n))
