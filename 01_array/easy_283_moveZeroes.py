from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r, size = 0, 0, len(nums)
        while r < size:
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l+=1
            r+=1
        print(nums)

    def moveZeroes1(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size, l = len(nums), 0
        for i in range(0, size):
            if nums[i] != 0:
                nums[l] = nums[i]
                l += 1
        for i in range(l, size):
            nums[i] = 0


s = Solution()
nums = [0, 1, 0, 3, 12]

print('res: ', s.moveZeroes(nums))
