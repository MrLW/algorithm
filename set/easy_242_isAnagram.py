class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        record = [0 for _ in range(26)]
        for e in s:
            record[ord(e)-ord('a')] += 1
        for f in t:
            record[ord(f)-ord('a')] -= 1
        for r in record:
            if r != 0:
                return False
        return True


s = "bbab"
t = "abbb"

solution = Solution()
print('res', solution.isAnagram(s,t))
