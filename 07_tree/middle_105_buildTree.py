# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        index = {element: i for i, element in enumerate(inorder)}

        def buildTree(preorder: List[int], inorder: List[int]) -> TreeNode:
            if not (preorder and inorder):
                return None
            root = TreeNode(preorder[0])

            mid_idx = index[preorder[0]]

            root.left = self.buildTree(
                preorder[1:mid_idx+1], inorder[:mid_idx])

            root.right = self.buildTree(
                preorder[mid_idx + 1:], inorder[mid_idx+1:])
            return root
        return buildTree(preorder, inorder)


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]

s = Solution()
res = s.buildTree(preorder, inorder)
print(res)
