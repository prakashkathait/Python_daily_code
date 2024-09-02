class Solution(object):
    def differenceOfSum(self, nums):
        s1 = sum(nums)
        s2=0
        for i in range(len(nums)):
            while(nums[i]!=0):
                s2 +=nums[i]%10
                nums[i] = nums[i]//10
        return abs(s1-s2)