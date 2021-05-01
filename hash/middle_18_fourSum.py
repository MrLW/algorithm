from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        hashtableA = dict()

        nums1 = [x for x in nums if x <= 0]

        for i in range(0, len(nums1)):
            for j in range(i+1, len(nums1)):
                if nums[i]+nums[j] not in hashtableA:
                    hashtableA[nums[i]+nums[j]] = []
                hashtableA[nums[i]+nums[j]].append(nums[i])
                hashtableA[nums[i]+nums[j]].append(nums[j])

        nums2 = [x for x in nums if x > 0]
        res = []
        for m in range(0, len(nums2)):
            for n in range(m+1, len(nums2)):
                if target - nums2[m] - nums2[n] in hashtableA:
                    t = hashtableA[target - nums2[m] - nums2[n]]
                    for k in range(0, 2, len(t)):
                        res.append(
                            [nums2[m], nums2[n], hashtableA[k], hashtableA[k+1]])
        return res


s = Solution()
nums, target = [1, 0, -1, 0, -2, 2], 0
s.fourSum(nums, target)
