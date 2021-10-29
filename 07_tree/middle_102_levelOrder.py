# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
    
        def levelOrder(lRoot: TreeNode, rRoot: TreeNode, level: int):
            # 针对空节点的判断
            if not lRoot and not rRoot:
                return
            if not level:
                if level != len(res):
                    res[level].append(lRoot.val)
                else:
                    res.append([lRoot.val])
            else:
                if lRoot:
                    if level != len(res):
                        res[level].append(lRoot.val)
                    else:
                        res.append([lRoot.val])
                if rRoot:
                    if level != len(res):
                        res[level].append(rRoot.val)
                    else:
                        res.append([rRoot.val])
            if level:
                if lRoot:
                    levelOrder(lRoot.left, lRoot.right, level+1)
            if rRoot:
                levelOrder(rRoot.left, rRoot.right, level+1)

        levelOrder(root, root, 0)
        return res


root = TreeNode(1)

root.left = TreeNode(2)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)

# root.right = TreeNode(20)
# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)


s = Solution()
s.levelOrder(root)
