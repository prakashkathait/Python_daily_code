class Solution(object):
    def missingNumber(self, nums):
        nums.sort()
        a = 0
        i = 0  
        for i in range(len(nums)):
            if nums[i] == a:
                a += 1
            else:  
                return a
        return a