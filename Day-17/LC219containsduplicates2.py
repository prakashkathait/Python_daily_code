class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        for i in range(len(nums)):
            for j in range(len(nums)):
                if (i==j):
                    continue
                if (nums[i]==nums[j] and abs(i-j)<=k):
                    return True 
        return False
