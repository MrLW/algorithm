class Solution:

    def getNext(self, s: str):
        j, next = -1, [-1 for _ in range(0, len(s))]
        for i in range(1, len(s)):
            # 如果前后缀不相同
            while j >= 0 and s[i] != s[j+1]:
                j = next[j]

            # 如果前后缀相同, 则前缀j+1
            if s[j+1] == s[i]:
                j += 1
            next[i] = j
        return next

    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        j, next = -1, self.getNext(needle)
        for i in range(0, len(haystack)):
            while j >= 0 and haystack[i] != needle[j+1]:
                j = next[j]
            if haystack[i] == needle[j+1]:
                j += 1
            if j == len(needle) - 1:
                return i - len(needle) + 1
        return -1


haystack, needle = "", ""
s = Solution()
print('res: ', s.strStr(haystack, needle))
