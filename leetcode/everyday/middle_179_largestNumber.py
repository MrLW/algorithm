from typing import List
from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        '''
        给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。
        注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数
        '''
        def compare(a: int, b: int):
            sa, sb = 10, 10
            while sa <= a:
                sa *= 10
            while sb <= b:
                sb *= 10
            return (sa * b + a) - (sb * a + b)
        nums.sort(key=cmp_to_key(compare))
        res = "".join([str(n) for n in nums])
        return res if res[0] != '0' else '0'


s = Solution()
nums = [0, 1]
print('res', s.largestNumber(nums))
