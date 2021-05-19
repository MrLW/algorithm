import collections


class Solution:
    def reverseWords(self, s: str) -> str:
        left, right = 0, len(s)-1
        while left <= right:
            if s[left] != ' ':
                break
            left += 1
        while left <= right:
            if s[right] != ' ':
                break
            right -= 1
        res, word = collections.deque(), []
        while left <= right:
            if s[left] == ' ' and word:
                res.appendleft(''.join(word))
                word = []
            elif s[left] != ' ':
                word.append(s[left])
            left += 1
        # 增加最后一个单词
        res.appendleft("".join(word))
        return " ".join(res)


solution = Solution()
s = "a good   example"
print('res: ', solution.reverseWords(s))
