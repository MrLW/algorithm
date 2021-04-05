from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        '''
        88. 合并两个有序数组
        '''

        # 2. 原地排序
        k = m + n - 1
        while m > 0 and n > 0 :
            if nums1[m - 1] > nums2[n - 1]:
                nums1[k] = nums1[m-1]
                m-=1
            else :
                nums1[k] = nums2[n-1]
                n-=1
            k-=1
        nums1[:n] = nums2[:n]

        # 1. 增加一个数组来实现
        # sorted, i, j, x = [0 for _ in range(m+n)], 0, 0, 0
        # while i < m or j < n:
        #     if j >= n:
        #         sorted[x] = nums1[i]
        #         x += 1
        #         i += 1
        #     elif i >= m:
        #         sorted[x] = nums2[j]
        #         x += 1
        #         j += 1
        #     elif nums1[i] <= nums2[j]:
        #         sorted[x] = nums1[i]
        #         i += 1
        #         x += 1
        #     else:
        #         sorted[x] = nums2[j]
        #         j += 1
        #         x += 1
        # nums1[:] = sorted


# num1 = [1,2,5,7,0,0,0,0]
# num2 = [2,4,5,6]
#
#  =>
# num1 = [1,2,2,7,0,0,0,0] t = 5
# num2 = [2,4,5,6]
# min(nums1[i], nums2[j], t)
[1, 2, 3, 0, 0, 0]
3
[2, 5, 6]
3

s = Solution()
nums1, m, nums2, n = [1, 2, 3, 0, 0, 0], 3,  [2, 5, 6], 3
# nums1, m, nums2, n = [1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3
s.merge(nums1, m, nums2, n)
