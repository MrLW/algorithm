class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums = sorted(nums)
        res = list()
        for i in range(0, len(nums)):
            if nums[i] > 0:
                return res
            left = i+1
            right = len(nums)-1
            # 这里必须是 i == i-1, 不能是 i == i+1来判断
            # 并且这种判断也只能针对 3元素相加
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while left < right:
                if nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    while left + 1 < len(nums) and nums[left] == nums[left + 1]:
                        left += 1
                    while right-1 > 0 and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
        return res
