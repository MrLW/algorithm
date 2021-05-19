from typing import List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - nums[i] in hashtable:
                return [hashtable[target-nums[i]], i]
            hashtable[nums[i]] = i
        return []


s = Solution()
nums, target = [2, 7, 11, 15], 10
print('res', s.twoSum(nums, target))
