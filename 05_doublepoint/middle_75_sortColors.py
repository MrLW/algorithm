from typing import List


class Solution:

    def sortColors(self, nums: List[int]) -> None:
        """
        75. 颜色分类: 
            给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
            此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

        """
        # 双指针
        i, p0, p2 = 0, 0, len(nums)-1
        while i <= p2:
            # 核心: 一定要先执行while == 2，再执行 if == 0
            while nums[i] == 2 and i < p2:
                nums[p2], nums[i] = nums[i], nums[p2]
                p2 -= 1
            if nums[i] == 0:
                nums[p0], nums[i] = nums[i], nums[p0]
                p0 += 1
            i += 1

    def sortColors2(self, nums: List[int]) -> None:
        """
        75. 颜色分类: 
            给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
            此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

        """
        # 单指针 + 2*for
        head = 0
        for i in range(0, len(nums)):
            if nums[i] == 0:
                nums[i], nums[head] = nums[head], nums[i]
                head += 1
        for j in range(head, len(nums)):
            if nums[j] == 1:
                nums[j], nums[head] = nums[head], nums[j]
                head += 1


nums = [1, 2, 0]

s = Solution()
s.sortColors(nums)
print('nums', nums)
