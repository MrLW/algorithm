# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        '''
            # 递归实现
            if root is None:
                return []
            res = []
            res.append(root.val)
            res.extend(self.inorderTraversal(root.left))
            res.extend(self.inorderTraversal(root.right))
            return res
        '''
        '''
            # 迭代实现
            思路: 
                1. 用一个栈来维护从上到下的访问路径，递归只是隐形的维护，迭代需要我们自己维护
                2. 我们只需要着重处理左节点or右节点 + 根节点 即可, 右节点or左节点 我们可以再让其变成根节点进行处理
            stack, res = [], []
            while root is None or len(stack) != 0:
                while root is not None:
                    stack.append(root)
                    root = root.left
                root = stack.pop()
                res.append(root.val)
                root = root.right
            return res
        '''
        