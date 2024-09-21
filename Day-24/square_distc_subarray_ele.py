class Solution(object):
    def sumCounts(self, nums):
        tot = 0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                tot += len(set(nums[i:j+1])) ** 2
        return tot