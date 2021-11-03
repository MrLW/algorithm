from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
            动态方程: 
                dp[i]=min(dp[i−1]+cost[i−1],dp[i−2]+cost[i−2])
            n = len(cost)
            dp = [0] * (n+1)
            dp[0] = dp[1] = 0
            for i in range(2, n+1):
                dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
            return dp[n]
        '''
        n = len(cost)
        pre = cur = 0
        for i in range(2, n+1):
            next = min(cur+cost[i-1], pre+cost[i-2])
            pre = cur
            cur = next
        return cur


cost = [10, 15]
s = Solution()
s.minCostClimbingStairs(cost)
