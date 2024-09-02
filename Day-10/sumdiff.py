class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        """
        :type nums: List[int]
        :type diff: int
        :rtype: int
        """
        triplets=0 
        for ele in range(len(nums)-1, -1, -1):
            if (nums[ele] - diff) and (nums[ele] - (diff*2)) in nums:
                triplets +=1
        return triplets