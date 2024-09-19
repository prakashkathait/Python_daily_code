class Solution(object):
    def maxProduct(self, nums):
        res = 0
        n = len(nums)
        curr_max = nums[0]
        for i in range(1,n):
            res = max(res,((nums[i]-1)*(curr_max-1)))
            curr_max = max(curr_max,nums[i])
        return res

 