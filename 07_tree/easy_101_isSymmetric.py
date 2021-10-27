# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isSymmetric(left: TreeNode, right: TreeNode) -> bool:
            if not left and not right:
                return True
            if(not left) ^ (not right):
                return False
            if left.val != right.val:
                return False
            return isSymmetric(left.left, right.right) and isSymmetric(left.right, right.left)
        return isSymmetric(root, root) if root else True


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(2)

d = TreeNode(2)
f = TreeNode(2)
a.left = b
a.right = c
b.left = d
c.left = f
s = Solution()
print(s.isSymmetric(a))
