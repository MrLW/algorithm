from typing import List
from typing import Counter


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        '''
        题目: 781. 森林中的兔子
        '''
        # 1. 利用规律实现
        count = Counter(answers)
        res = sum([(x+y) // (y+1) * (y+1) for y, x in count.items()])
        # 1. for + dic
        # res, i, size, dic = 0, 0, len(answers), dict()
        # for i in range(size):
        #     if answers[i] == 0:
        #         res += 1
        #     elif answers[i] not in dic or dic[answers[i]] == 0:
        #         dic[answers[i]] = answers[i]
        #         res += answers[i] + 1
        #     elif dic[answers[i]] > 0:
        #         dic[answers[i]] -= 1
        # return res


s, answers = Solution(), [0, 0, 2, 2, 1]
# [1, 1, 1] => 2+2 = 4
# [2, 2, 2] => 3 只 兔子 回答 2 => 3 / 2+1 = 1
print('res', s.numRabbits(answers))
