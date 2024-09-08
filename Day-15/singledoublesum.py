class Solution(object):
    def canAliceWin(self, nums):
        singlesum =0
        doublesum =0
        for num in nums:
            if num<10:
                singlesum+= num
            else:
                doublesum += num
        return singlesum != doublesum