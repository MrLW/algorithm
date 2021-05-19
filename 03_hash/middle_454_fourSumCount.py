from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        hashtableAB, res = dict(), 0
        for i, num1 in enumerate(nums1):
            for j, num2 in enumerate(nums2):
                if num1+num2 not in hashtableAB:
                    hashtableAB[num1+num2] = 0
                hashtableAB[num1+num2] += 1
        for num3 in nums3:
            for num4 in nums4:
                if -(num3+num4) in hashtableAB:
                    res += hashtableAB[-(num3+num4)]
        return res


A = [1, 2, 3]
B = [-2, -1, -2]
C = [-1, 2, 0]
D = [0, 2, -1]

s = Solution()
print('res', s.fourSumCount(A, B, C, D))
