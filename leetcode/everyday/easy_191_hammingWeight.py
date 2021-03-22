class Solution:
    def hammingWeight(self, n: int) -> int:
        '''
        位1的个数
        '''
        # result = 0

        ret = 0
        while n:
            n &= n-1
            ret += 1
        return ret

        # result = 0
        # for e in bin(n)[2:]:
        #     result += (int(e) & 1)
        # return result


s = Solution()
n = 0b00000000000000000000000000001011
x = 0b11111111111111111111111111111111

print('result', s.hammingWeight(n))
