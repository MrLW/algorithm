from typing import List
import collections


class Solution:

    def totalFruit(self, tree):
        ans = i = 0
        count = collections.Counter()
        for j, x in enumerate(tree):
            count[x] += 1
            while len(count) >= 3:
                count[tree[i]] -= 1
                if count[tree[i]] == 0:
                    del count[tree[i]]
                i += 1
            ans = max(ans, j - i + 1)
        return ans

    def totalFruit2(self, tree: List[int]) -> int:
        l, r, maxCount, size = 0, 0, 0, len(tree)
        if size <= 2:
            return size
        # 篮子里分别装的东西, 初始化为-1
        a, b = -1, -1
        while l < size and r < size:
            if a == -1:
                a = tree[r]
                maxCount = max(maxCount, r-l+1)
                r += 1
            elif tree[r] == a:
                maxCount = max(maxCount, r-l+1)
                r += 1
            elif b == -1:
                b = tree[r]
                maxCount = max(maxCount, r-l+1)
                r += 1
            elif tree[r] == b:
                maxCount = max(maxCount, r-l+1)
                r += 1
            else:
                l = r-1
                while l > 0 and tree[l] == tree[l-1]:
                    l = l-1
                a = tree[l]
                b = tree[r]
        return maxCount


s = Solution()
tree = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]
print('res: ', s.totalFruit(tree))
