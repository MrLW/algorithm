# 七. 二叉树

## ① 二叉树

### 7.1.1 相同的二叉树

##### 1. 递归

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

##### 2. 广度优先搜索(TODO)

```python

```



### 7.1.2 对称二叉树

##### 1. 递归实现

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

##### 2. 迭代实现

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





## ②、叉搜索树

##### 前言: 二叉搜索树的特性:

- 中序遍历时序列一定是升序的, 有些题目可以利用这个性质

### 7.2.1 二叉树的前中后序遍历

### 7.2.2 二叉搜索树的个数(动态规划)

### 7.2.3 二叉搜索树的数组(回溯法)

### 7.2.4 验证二叉搜索树(中序遍历)

#####    1. 中序遍历 + 栈

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

##### 2. 中序遍历+递归

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

##### 3. 递归

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



### 7.2.5 恢复二叉树

##### 1. 中序遍历+栈

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

##### 2. Minor 中序遍历实现(TODO)





## 深度/广度优先搜索(TODO)







<!-- √ ×-->
<escape>

  <table>
  <tr>
    <th colspan="2">名称</th>
    <th >完成</th>
    <th>时间复杂度</th>
    <th>空间复杂度</th>
  </tr>
  <tr>
    <td rowspan="8">排序</td>
    <td align="center">选择排序</td>
    <td align="center">√</td>
    <td align="center">O(n^2)</td>
    <td align="center">O(n)</td>
  </tr>
  <tr>
    <td>快速排序</td>
    <td align="center">√</td>
    <td align="center">未知</td>
    <td align="center">未知</td>
  </tr>
   <tr>
    <td>冒泡排序</td>
    <td align="center">√</td>
        <td align="center">未知</td>
    <td align="center">未知</td>
  </tr>
   <tr>
    <td>插入排序</td>
    <td align="center">√</td>
        <td align="center">未知</td>
    <td align="center">未知</td>
  </tr>
   <tr>
    <td>堆排序</td>
    <td align="center">×</td>
        <td align="center">未知</td>
    <td align="center">未知</td>
  </tr>
  <tr>
    <td>希尔排序</td>
    <td align="center">×</td>
        <td align="center">未知</td>
    <td align="center">未知</td>
  </tr>
  <tr>
    <td>归并排序</td>
    <td align="center">×</td>
        <td align="center">未知</td>
    <td align="center">未知</td>
  </tr>
   <tr>
    <td>基数排序</td>
    <td align="center">×</td>
    <td align="center">未知</td>
    <td align="center">未知</td>
  </tr>
  <tr>
    <td rowspan="3">查找</td>
    <td>二分查找</td>
    <td align="center">×</td>
    <td align="center">未知</td>
    <td align="center">未知</td>
  </tr>
  <tr>
    <td>分块查找</td>
    <td align="center">×</td>
    <td align="center">未知</td>
    <td align="center">未知</td>
  </tr>
  <tr>
    <td >顺序查找</td>
    <td align="center">×</td>
    <td align="center">未知</td>
    <td align="center">未知</td>
  </tr>
</table>
</escape>