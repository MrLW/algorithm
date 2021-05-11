from typing import List


class Solution:

    def removeElement(self, nums: List[int], val: int) -> int:
        size, l = len(nums), 0
        for i in range(0, size):
            if nums[i] != val:
                nums[l] = nums[i]
                l+=1
        return l

    def removeElement2(self, nums: List[int], val: int) -> int:
        size, valCount, c = len(nums), nums.count(val), 0
        for i in range(0, size):
            if nums[i] == val:
                c += 1
            else:
                nums[i-c] = nums[i]
        return size - valCount


nums, val = [3, 2, 2, 3, 2, 2], 3
s = Solution()
print('res', s.removeElement(nums, val))
