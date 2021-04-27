from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        size, l = len(nums), 0
        for r in range(0, size):
            if nums[l] != nums[r]:
                l += 1
                nums[l] = nums[r]
        return l+1


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
s = Solution()
print('res', s.removeDuplicates(nums))
