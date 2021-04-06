from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        题目:删除有序数组中的重复项 II
        '''
        # 2. 双指针
        return self.process(nums, 2)

    def process(self, nums: List[int], k: int):
        u = 0
        for n in nums:
            if u < k or nums[u-k] != n:
                nums[u] = n
                u += 1
        return u
        # 1. while 遍历
        # size = len(nums)
        # if size <= 2: return size
        # first, second, cur = nums[0], nums[1], 2
        # while cur < size:
        #     if first == second and second == nums[cur]:
        #         i = cur
        #         j = i+1
        #         while j < size:
        #             if nums[j] != nums[i]:
        #                 break
        #             j += 1
        #         while j < size:
        #             nums[i] = nums[j]
        #             j += 1
        #             i += 1
        #         size = i
        #     cur += 1
        #     first = nums[cur-2]
        #     second = nums[cur-1]
        # return size


s = Solution()
nums = [0, 0, 1, 1, 1, 1, 1, 1, 2, 3, 3, 3, 4, 5, 5, 5, 6, 7, 7, 7, 8]
print('res: ', s.removeDuplicates(nums))
