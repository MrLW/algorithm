class Solution:

    def get_sum(self, n):
        total = 0
        while n > 0:
            n, digit = divmod(n, 10)
            total += digit ** 2
        return total

    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.get_sum(n)
        while slow != fast and fast != 1:
            slow = self.get_sum(slow)
            fast = self.get_sum(self.get_sum(fast))
        return fast == 1
        
    def isHappy2(self, n: int) -> bool:
        s = set()
        while n != 1 and n not in s:
            s.add(n)
            n = self.get_sum(n)
        return n == 1


s = Solution()
n = 19
print('res:', s.isHappy(n))
