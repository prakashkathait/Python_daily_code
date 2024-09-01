class Solution(object):
    def minimumAverage(self, nums):
        nums.sort()
        res=100
        for i in range(len(nums)//2):
            res=min(res,(nums[i]+nums[len(nums)-i-1])/2.0)
        return res