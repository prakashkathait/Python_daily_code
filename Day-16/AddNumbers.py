class Solution(object):
    def twoSum(self, nums, target):
        #creating a dictionary to store the number and there corresponding indices 
        n={}
        #looping through the array
        for i,num in enumerate(nums):
            #calculating the difference between the current number and the target
            diff = target-num
            #if difference in dict. then return the indices and the number that add up to the target 
            if diff in n:
                return [i,n[diff]]
            #if doesn't exists, add the current number and its index in the dict.
            n[num] = i
            #if no two numbers add up to the target, returning None 
        return None
      