import math
from typing import List


class Solution:
    # [start, end): 左闭右开
    def reverse(self, sList: List, start, end):
        mid = start + (end-start) // 2
        while start < mid:
            sList[start], sList[end-1] = sList[end-1], sList[start]
            start += 1
            end -= 1

    def reverseStr(self, s: str, k: int) -> str:
        '''
        反转字符串 II: 给定一个字符串 s 和一个整数 k，你需要对从字符串开头算起的每隔 2k 个字符的前 k 个字符进行反转
        '''
        i = 0
        sList = list(s)
        for i in range(0, len(sList), 2*k):
            if i+k > len(sList):
                self.reverse(sList, i, len(sList))
            else:
                self.reverse(sList, i, i+k)
        return "".join(sList)


s, k = "hyzqyljrnigxvdtneasepfahmtyhlohwxmkqcdfehybknvdmfrfvtbsovjbdhevlfxpdaovjgunjqlimjkfnqcqnajmebeddqsgl", 39
solution = Solution()
print('res: ', solution.reverseStr(s, k))
