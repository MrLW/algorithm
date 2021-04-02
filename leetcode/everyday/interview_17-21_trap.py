from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        面试题 17.21. 直方图的水量
        '''

        # 1. 单调栈
        stack, size, res = [], len(height), 0
        for i in range(size):
            while stack and height[stack[-1]] < height[i]:
                top = stack.pop()
                if not stack:
                    break
                left = stack[-1]
                w = i-left-1
                h = min(height[i], height[left]) - height[top]
                res += w*h

            stack.append(i)
        return res
        # 2. 双指针
        # res = 0
        # size = len(height)
        # leftMax, rightMax = 0, 0
        # left, right = 0, size-1
        # while left < right:
        #     leftMax = max(leftMax, height[left])
        #     rightMax = max(rightMax, height[right])
        #     if height[left] < height[right]:
        #         res += leftMax-height[left]
        #         left += 1
        #     else:
        #         res += rightMax-height[right]
        #         right -= 1
        # return res

        # 3. 动态规划解法
        # size = len(height)
        # if size == 0:
        #     return 0
        # leftMax, rightMax = [0 for _ in range(size)], [0 for _ in range(size)]
        # leftMax[0], rightMax[size-1] = height[0], height[size-1]
        # for i in range(1, size):
        #     leftMax[i] = max(leftMax[i-1], height[i])
        # for j in range(size-2, -1, -1):
        #     rightMax[j] = max(rightMax[j+1], height[j])
        # res = 0
        # for v in range(size):
        #     res+=min(leftMax[v], rightMax[v])-height[v]
        # return res


s = Solution()
nums = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print('res', s.trap(nums))
