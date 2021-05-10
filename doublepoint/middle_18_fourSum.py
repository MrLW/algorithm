from typing import List


class Solution:

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        size = len(nums)
        if size < 4:
            return []
        res = []
        for i in range(0, len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            if nums[i] + nums[size-1] + nums[size-2] + nums[size-3] < target:
                continue
            for j in range(i+1, size - 2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                    break
                if nums[i] + nums[j] + nums[size-1] + nums[size-2] < target:
                    continue

                left, right = j+1, size-1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total > target:
                        right -= 1
                    if total < target:
                        left += 1
                    if total == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                        left+=1
                        right-=1
        return res


s = Solution()
nums = [1, 0, -1, 0, -2, 2]
s.fourSum(nums, 0)
