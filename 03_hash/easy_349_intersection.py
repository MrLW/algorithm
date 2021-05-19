from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return set(nums1).intersection(set(nums2))


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
s = Solution()

print('res', s.intersection(nums1, nums2))