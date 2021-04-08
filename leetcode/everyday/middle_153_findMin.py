from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        已知一个长度为 n 的数组，预先按照升序排列，经由 1 到 n 次 旋转 后，得到输入数组。例如，原数组 nums = [0,1,2,4,5,6,7] 在变化后可能得到：
        若旋转 4 次，则可以得到 [4,5,6,7,0,1,2]
        若旋转 4 次，则可以得到 [0,1,2,4,5,6,7]
        注意，数组 [a[0], a[1], a[2], ..., a[n-1]] 旋转一次 的结果为数组 [a[n-1], a[0], a[1], a[2], ..., a[n-2]] 。
        给你一个元素值 互不相同 的数组 nums ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 最小元素 
        '''
        l, r, = 0, len(nums)-1
        if r == 0:
            return nums[0]

        while l <= r:
            mid = l + (r-l)//2
            if nums[l] >= nums[mid] >= nums[r]:
                return nums[r]
            if nums[l] <= nums[mid] <= nums[r]:
                return nums[l]
            elif nums[l] < nums[mid]:
                l = mid 
            elif nums[mid] < nums[r]:
                r = mid
        return nums[l]


#    [0,1,2,3,4,5,6,7,8]
# => [2,3,4,5,6,7,8,0,1]
# => [7,8,0,1,2,3,4,5,6]
s = Solution()
nums =  [7,8,0,1,2,3,4,5,6]
print('res', s.findMin(nums))
