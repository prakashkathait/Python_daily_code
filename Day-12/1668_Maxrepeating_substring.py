class Solution(object):
    def maxRepeating(self, sequence, word):
        k = 1
        while word * k in sequence:
            k += 1
        return k - 1