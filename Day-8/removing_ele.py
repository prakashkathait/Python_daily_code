class Solution(object):
    def minOperations(self, nums, k):
        nums.sort()
        cnt =0    
        for num in nums:
            if num>=k:
                break
            else:
                cnt +=1
        return cnt 