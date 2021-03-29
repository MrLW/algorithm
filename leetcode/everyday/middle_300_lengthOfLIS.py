from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        题目: 
            思路: 动态规划, dp[i] = dp[j] + 1
        '''
        size = len(nums)
        if size == 0: return 0
        dp = [1 for _ in range(size)]
        res = 1
        for i in range(1, size):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
            res = max(res, dp[i])
        return res
            
        


nums = [10, 4, 9, 11, 1, 13, 14, 15, 2, 5, 3, 7, 101, 18]
s = Solution()
print('res:', s.lengthOfLIS(nums))
