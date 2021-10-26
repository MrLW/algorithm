# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack, pre = [], TreeNode(float("-inf"))
        a, b = None, None
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if cur.val < pre.val:
                if not a:
                    a = pre
                b = cur
            pre = cur
            cur = cur.right
        a.val, b.val = b.val, a.val


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.left.right = TreeNode(2)
    Solution().recoverTree(root)
