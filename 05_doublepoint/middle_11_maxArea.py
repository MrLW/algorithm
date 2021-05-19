from typing import List


class Solution:

    def maxArea(self, height: List[int]) -> int:
        '''双指针'''
        res, l, r = 0, 0, len(height)-1
        while l <= r:
            if height[l] >= height[r]:
                res = max(res, height[r]*(r-l))
                r -= 1
            else:
                res = max(res, height[l]*(r-l))
                l+=1
        return res

    def maxArea2(self, height: List[int]) -> int:
        '''暴力法'''
        res = 0
        for i in range(len(height)-1):
            for j in range(i+1, len(height)):
                h = min(height[i], height[j])
                res = max(res, h * (j-i))
        return res


s = Solution()
height = [ 8, 6, 2, 5, 4, 8, 3]
print('res', s.maxArea(height))
print('res', s.maxArea2(height))
