class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
            无重复字符的最长子串: 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度
        '''
        size = len(s)
        if size <= 1:
            return size
        res, left, right = 1, 0, 1
        while right < size:
            if s[right] not in s[left: right]:
                res = max(res, right - left + 1)
                right += 1
            else:
                t = right - 1
                while t > left and s[t] != s[right]:
                    t -= 1
                left = t + 1

        return res

solution = Solution()
s = "pwwkew"
solution.lengthOfLongestSubstring(s)
