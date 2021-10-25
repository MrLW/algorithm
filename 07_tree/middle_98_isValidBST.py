# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    '''
        题目: 验证二叉搜索树
    '''
    # pre = float('-inf')

    def isValidBST(self, root: TreeNode) -> bool:

        # 1. 中序遍历 + 栈
        stack, inorder  = [], float('-inf')
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right
        return True

        # 2. 中序遍历 + 递归
        # if not root:
        #     return True
        # if not self.isValidBST(root.left):
        #     return False
        # if root.val <= self.pre:
        #     return False
        # self.pre = root.val
        # return self.isValidBST(root.right)

        # 3. 递归
        # def isValidBST(root: TreeNode, lower=float('-inf'), upper=float('+inf')) -> bool:
        #     if not root:
        #         return True
        #     val = root.val
        #     if val <= lower or val >= upper:
        #         return False
        #     if not isValidBST(root.right, val, upper):
        #         return False
        #     if not isValidBST(root.left, lower, val):
        #         return False
        #     return True
        # return isValidBST(root)


_47 = TreeNode(47, None, TreeNode(56, None, None))
_26 = TreeNode(26, TreeNode(19, None, None))
root = TreeNode(32, _26, _47)

# [32,26,47,19,null,null,56,null,27]

s = Solution()

print('isValidBST: ', s.isValidBST(root))
