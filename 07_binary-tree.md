# 一、普通二叉树

### 1 相同的二叉树

##### 1.1、 递归

```python
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
```

##### 1.2 广度优先搜索(TODO)

```python

```



### 2 对称二叉树

##### 2.1、 递归实现

```python
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
```

##### 2.2、 迭代实现

```python
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def check(u, v) -> bool:
            queue = [u, v]
            while queue:
                u, v = queue.pop(), queue.pop()
                if not u and not v:
                    continue
                if (not u or not v) or u.val != v.val:
                    return False
                queue.append(u.left)
                queue.append(v.right)
                queue.append(u.right)
                queue.append(v.left)
            return True
        return check(root, root) if root else True
```



### 3 二叉树的层级

##### 3.1、 递归实现

```python

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
```



##### 3.2、 广度优先搜索(TODO)

```

```







# 二、二叉搜索树

### 前言: 二叉搜索树的特性:

- 中序遍历时序列一定是升序的, 有些题目可以利用这个性质

### 1、 二叉树的前中后序遍历

### 2、 二叉搜索树的个数(动态规划)

### 3、 二叉搜索树的数组(回溯法)

### 4、 验证二叉搜索树(中序遍历)

#####    4.1、 中序遍历 + 栈

```python
def isValidBST(self, root: TreeNode) -> bool:

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
```

##### 4.2、 中序遍历+递归

```python
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        if not self.isValidBST(root.left):
            return False
        if root.val <= self.pre:
            return False
        self.pre = root.val
        return self.isValidBST(root.right)
```

##### 4.3、 递归

```python
    def isValidBST(self, root: TreeNode) -> bool:
        def isValidBST(root: TreeNode, lower=float('-inf'), upper=float('+inf')) -> bool:
            if not root:
                return True
            val = root.val
            if val <= lower or val >= upper:
                return False
            if not isValidBST(root.right, val, upper):
                return False
            if not isValidBST(root.left, lower, val):
                return False
            return True
        return isValidBST(root)
```



### 5 恢复二叉树

##### 5.1、 中序遍历+栈

```python
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
```

##### 5.2、 Minor 中序遍历实现(TODO)





## 深度/广度优先搜索(TODO)