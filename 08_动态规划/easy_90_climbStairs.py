class Solution:
    def climbStairs(self, n: int) -> int:
        '''
            动态方程: dp[n] = dp[n-1] + dp[n-2]
            利用滚动数组实现, 可以省去建立DP的空间
        '''
        p = 0
        q = 0
        r = 1
        for _ in range(n):
            p = q
            q = r
            r = p+q
        return r


s = Solution()
n = 3
res = s.climbStairs(n)
print('res: ', res)
