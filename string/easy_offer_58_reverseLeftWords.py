class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        # 防止 n > 字符串长度
        if n >= len(s):
            return s
        return s[n:] + s[:n]


s, k = "abcdefg",  2
solution = Solution()
print('res: ', solution.reverseLeftWords(s, n))
