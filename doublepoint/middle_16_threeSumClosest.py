from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        '''
            题目: 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案
        '''
        nums = sorted(nums)
        res = sum(nums[0:3])
        for i in range(len(nums)-1):
            l, r = i+1, len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total < target:
                    l += 1
                elif total > target:
                    r -= 1
                elif total == target:
                    return total

                if abs(res-target) > abs(total-target):
                    res = total
        return res


s = Solution()
nums, target = [4,5,7,9], 11
'''
-4 -1 1 2
'''
print('res: ',s.threeSumClosest(nums, target))
