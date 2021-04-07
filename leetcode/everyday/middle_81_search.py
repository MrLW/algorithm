from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        # 二分查找
        l, r, n = 0, len(nums)-1, len(nums)
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return True
            if nums[0] <= nums[mid]:
                # 左边有序
                if nums[0] <= target < nums[mid]:
                    r = mid-1
                else:
                    l = mid+1
            else:
                # 右边有序
                if nums[mid] < target <= nums[n-1]:
                    l = mid+1
                else:
                    r = mid-1
        return False
        # p, size = len(nums), 0
        # 1. 这里还是用了O(n)的时间复杂度,草率了
        # for p in range(size-1):
        #     if nums[p] > nums[p+1]:
        #       break
        # 2步二分查找
        # return self.binarySearch(nums, 0, p, target) or self.binarySearch(nums, p+1, size-1, target)

    def binarySearch(self, nums: List[int], start: int, end: int, target: int):
        if start > end:
            return False
        middle = start + (end-start) // 2
        if nums[middle] == target:
            return True
        if nums[middle] > target:
            return self.binarySearch(nums, start, middle-1, target)
        if nums[middle] < target:
            return self.binarySearch(nums, middle+1, end, target)
        return False


s = Solution()
nums = [4, 5, 6, 7, 0, 1, 2]
# 4,5,6,7,8,0,1,2,3
print('res', s.search(nums, 0))
