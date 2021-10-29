# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:

        def maxDepth(lRoot: TreeNode, rRoot: TreeNode, depth) -> int:
            if not lRoot and not rRoot:
                return depth
            if lRoot or rRoot:
                depth += 1
            lMax, rMax = depth, depth
            if lRoot:
                lMax = max(depth, maxDepth(lRoot.left, lRoot.right, depth))
            if rRoot:
                rMax = max(depth, maxDepth(rRoot.left, rRoot.right, depth))
            return max(lMax, rMax)
        return maxDepth(root, root, 0)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.right = TreeNode(6)
root.right.right.right = TreeNode(10)
s = Solution()
print('maxDepth: ', s.maxDepth(root))
