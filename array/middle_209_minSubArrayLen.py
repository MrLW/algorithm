from typing import List


class Solution:

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r, size, total = 0, 0, len(nums), 0
        minCount = size+1
        while l < size:
            if total >= target:
                minCount = min(minCount, r-l)
                total -= nums[l]
                l += 1
            else:
                if r == size:
                    break
                total += nums[r]
                r += 1
        return 0 if minCount > size else minCount


s = Solution()
target, nums = 7, [1, 1, 1, 1, 1, 1, 1, 1, 1]
print('res', s.minSubArrayLen(target, nums))
