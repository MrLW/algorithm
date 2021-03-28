# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: TreeNode):
        '''
        题目: 实现一个二叉搜索树迭代器类BSTIterator ，表示一个按中序遍历二叉搜索树（BST）的迭代器：
        思路1: 将二叉树在构造函数中使用中序变成数组

        '''
        self.data = []
        self.recursionMiddleorderTraversal(root)
        self.pos = 0

    def recursionMiddleorderTraversal(self, root: TreeNode):
        if root:
            self.recursionMiddleorderTraversal(root.left)
            self.data.append(root.val)
            self.recursionMiddleorderTraversal(root.right)

    def next(self) -> int:

        res = self.data[self.pos]
        self.pos += 1
        return res

    def hasNext(self) -> bool:
        return self.pos < len(self.data)
        # Your BSTIterator object will be instantiated and called as such:
        # obj = BSTIterator(root)
        # param_1 = obj.next()
        # param_2 = obj.hasNext()


left2 = TreeNode(9)
right2 = TreeNode(20)
left1 = TreeNode(3)
right1 = TreeNode(15, left2, right2)
root = TreeNode(7, left1, right1)

s = BSTIterator(root)
print(s.next())
print(s.next())
print(s.hasNext())
print(s.next())
print(s.hasNext())
print(s.next())
print(s.hasNext())
print(s.next())
print(s.hasNext())