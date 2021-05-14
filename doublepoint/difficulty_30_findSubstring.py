from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        '''
        串联所有单词的子串: 给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。
                         注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。

        '''
        # 暴力法(超时)
        res = list()
        size = sum([len(word) for word in words])
        for i in range(len(s)):
            # 用来判断s的子串是否满足要求, 只有当tmp为空时说明子串符合要求
            tmp = words.copy()
            # l: 正在遍历单词的左边界
            # r: 以 words 字符串数组 字符数量的右边界, 之所以+1, 因为s[l:index]是左闭右开
            # index:正在遍历的索引
            index, l, r = i, i, i+size+1
            while index < r:
                if s[l:index] not in tmp:
                    index += 1
                else:
                    tmp.remove(s[l:index])
                    l = index
            if len(tmp) == 0:
                res.append(i)
        return res


# 输出：[0,9]
s, words = "wordgoodgoodgoodbestword", ["word", "good", "best"]
solution = Solution()

print('res: ', solution.findSubstring(s, words))
