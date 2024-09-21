class Solution(object):
    def maxProductDifference(self, nums):
        nums.sort()
        n = len(nums)
        res = 0

        for i in range(1):
            prod1 = nums[i]*nums[i+1]
            for j in range(1):
                prod2 = nums[n-2]*nums[n-1]
            res = prod2-prod1
        return res