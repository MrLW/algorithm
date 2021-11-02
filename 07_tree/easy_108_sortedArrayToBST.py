# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        mid_idx = int(len(nums) / 2)
        root = TreeNode(nums[mid_idx])
        root.left = self.sortedArrayToBST(nums[0: mid_idx])
        root.right = self.sortedArrayToBST(nums[mid_idx+1:])
        return root


nums = [-10, -3, 0, 5, 9]


s = Solution()
root = s.sortedArrayToBST(nums)
print(root)
