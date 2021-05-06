from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        反转字符串: Do not return anything, modify s in-place instead.
        """
        size = len(s)
        for i in range(0, size//2):
            s[i], s[-(i+1)] = s[-(i+1)], s[i]
        print(s)


solution = Solution()
s = ["d", "e", "m", "o"]

solution.reverseString(s)
