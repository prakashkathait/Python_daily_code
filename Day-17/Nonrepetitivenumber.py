class Solution(object):
    def singleNumber(self, nums):
        #using the Bitwise XOR 
        ans=0
        for num in nums:
            ans ^= num
        return ans