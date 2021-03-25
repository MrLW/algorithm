from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        '''
        题目:
            给定一个整数序列：a1, a2, ..., an，一个132模式的子序列 ai, aj, ak 被定义为：当 i < j < k 时，ai < ak < aj。设计一个算法，当给定有 n 个数字的序列时，验证这个序列中是否含有132模式的子序列。
            注意：n 的值小于15000。
        思路1:
            暴力法, 通过3个while循环来实现, 但是超时, 所以尝试下可不可以只用减少一个循环来实现
        思路2: 
            单调栈
        '''

        # 单调栈: O(n)
        N = len(nums)
        leftMin = [float('inf')]*N
        for i in range(1, N):
            leftMin[i] = min(leftMin[i-1], nums[i-1])
        print(leftMin)
        # 暴力法: O(n**2)
        # numsi = nums[0]
        # for j in range(1, len(nums)):
        #     for k in range(len(nums)-1, j, -1):
        #         if numsi < nums[k] and nums[k] < nums[j]:
        #             return True
        #     numsi = min(numsi, nums[j])
        # return False

        # 暴力法: O(n**3) 超时
        # i, j, k = 0, 0, 0
        # while i < len(nums)-2:
        #     j = i + 1
        #     while j < len(nums)-1:
        #         k = j+1
        #         while k < len(nums):
        #             if nums[i] < nums[k] and nums[k] < nums[j]:
        #                 return True
        #             k += 1
        #         j += 1
        #     i += 1
        # return False

        # 失败
        # flat: 用来表明 nums 是否是一个递增 or 递减数列
        # flag = True
        # for i in range(len(nums)-1):
        #     flag &= nums[i] >= nums[i+1]
        #     # 说明不是递减数列
        #     if not flag:
        #         break

        # if not flag:
        #     flag = True
        #     for i in range(len(nums)-1):
        #         flag &= nums[i] <= nums[i+1]
        #         # 说明不是递增数列
        #         if not flag:
        #             break
        # return not flag


s = Solution()
nums = [5, 3, 2, 0]
print(s.find132pattern(nums))
