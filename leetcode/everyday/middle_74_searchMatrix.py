from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        题目:
            编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
            ①. 每行中的整数从左到右按升序排列。
            ②. 每行的第一个整数大于前一行的最后一个整数。
        思路: 将二维转换成1维数组
        '''
        if matrix[0][0] > target:
            return False
        elif matrix[-1][-1] < target:
            return False
        elif matrix[0][0] <= target and matrix[0][-1] >= target:
            # 数组的二分查找
            first, end = 0, len(matrix[0]) - 1
            while first <= end:
                # mid = (first + end) // 2
                mid = (end - first) // 2 + first
                if matrix[0][mid] == target:
                    return True
                elif matrix[0][mid] > target:
                    end = mid-1
                else:
                    first = mid+1
            return False

        else:
            return self.searchMatrix(matrix[1:], target)


matrix, target = [
    [1, 3, 5, 7],
    [10, 11, 16, 20]], 13
s = Solution()
print('res', s.searchMatrix(matrix, target))
