#1470. Shuffle the Array

class Solution(object):
    def shuffle(self, nums, n):
       res=[]
       i = 0
       for i in range(0, n):
          res.append(nums[i])
          res.append(nums[n+i])
       return res