class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 2:
            return 1
        p = 0
        q = r = 1
        for i in range(3, n + 1):
            s = p + q + r
            p, q, r = q, r, s
        return s


s = Solution()
res = s.tribonacci(30)
