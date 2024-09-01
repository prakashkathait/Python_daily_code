class Solution(object):
    def decompressRLElist(self, nums):
        res=[]
        n=len(nums)
        for i in range(0,n,2):
            freq = nums[i]
            val = nums[i+1]
            while freq:
                res.append(val)
                freq -=1
        return res