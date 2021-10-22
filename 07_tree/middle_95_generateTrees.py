from typing import List
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def generateTrees(start, end):
            if start > end:
                return [None, ]
            res = []
            for i in range(start, end+1):
                leftTrees = generateTrees(start, i-1)
                rightTrees = generateTrees(i+1, end)

                for l in leftTrees:
                    for r in rightTrees:
                        cur = TreeNode(i)
                        cur.left, cur.right = l,  r
                        res.append(cur)
            return res
        return generateTrees(1, n) if n else []


s = Solution()

res = s.generateTrees(3)
print(res)
