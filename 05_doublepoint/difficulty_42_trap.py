from typing import List


class Solution:

    def trap(self, height: List[int]) -> int:
        '''
            题目(接雨水): 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
        '''
        left, right = 0, len(height)-1
        res = 0
        left_max = right_max = 0
        while left <= right:
            if left_max < right_max:
                res += max(0, left_max-height[left])
                left_max = max(left_max, height[left])
                left+=1
            else:
                res += max(0, right_max-height[right])
                right_max = max(right_max, height[right])
                right-=1
        return res
                

    def trap2(self, height: List[int]) -> int:
        '''
            题目(接雨水): 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
        '''
        if len(height) <= 2:
            return 0
        res = 0
        left_max, right_max = [0 for _ in range(len(height))], [
            0 for _ in range(len(height))]
        left_max[0] = height[0]
        for i in range(1, len(height)):
            left_max[i] = max(height[i], left_max[i-1])
        right_max[-1] = height[-1]
        for j in range(len(height)-2, -1, -1):
            right_max[j] = max(height[j], right_max[j+1])
        for k in range(len(height)):
            res += min(left_max[k], right_max[k]) - height[k]
        return res


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
s = Solution()

s.trap(height)
