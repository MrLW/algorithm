import math


class Solution:
    def clumsy(self, N: int) -> int:
        stack, index = [N], 0
        N -= 1
        while N > 0:
            if index % 4 == 0:
                stack.append(stack.pop() * N)
            elif index % 4 == 1:
                ele = stack.pop()
                if ele > 0:
                    stack.append(math.floor(ele / N))
                else:
                    stack.append(math.ceil(ele / N))
            elif index % 4 == 2:
                stack.append(N)
            elif index % 4 == 3:
                stack.append(-N)
            N -= 1
            index += 1
        return sum(stack)


s = Solution()
print('res:', s.clumsy(10))


#  4 * 3 / 2 + 1
