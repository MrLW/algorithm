class Solution:
    def reverseBits(self, n: int) -> int:
        '''
        题目: 颠倒给定的 32 位无符号整数的二进制位
             如:
                输入:00000010100101000001111010011100
                输出:00111001011110000010100101000000
        思路: 
            1. 将res左移
            2. 获取二进制末尾数字
            3. 将res拼接末尾数字
            4. n右移
        '''
        res = 0
        for i in range(32):
            res <<= 1
            res |= n & 1
            n >>= 1
        return res


s = Solution()
n = 4294967293
print('res:', s.reverseBits(n))
