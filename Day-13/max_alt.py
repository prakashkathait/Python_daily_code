class Solution(object):
    def largestAltitude(self, gain):
        start = 0
        res = 0
        for first in gain:
            start += first
            res = max(res,start)
        return res