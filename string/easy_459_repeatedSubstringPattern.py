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

    def repeatedSubstringPattern(self, s: str) -> bool:
        size, next = len(s), self.getNext(s)
        if next[size-1] != -1 and size % (size - (next[size-1] + 1)) == 0:
            return True
        return False

    # 骚操作
    def repeatedSubstringPattern2(self, s: str) -> bool:
         return (s + s).find(s, 1) != len(s)


s = Solution()

'''
abcab

    => abababab
    s="abab", t = "abababab", i=2, n = 4

    s[0,n-1] = t[i:n+i-1]
=>  s[0,4-1] = t[2:4+2-1] =

    s[0:n-i-1] = t[i:n-1]
=>  s[0:4-2-1] = t[2:4-1]
=>  s[0,1]
    


    => babababa


'''
s.repeatedSubstringPattern("abab")
