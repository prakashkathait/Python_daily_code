class Solution(object):
    def numberOfMatches(self, n):
        mat = 0
        while n>1:
            if n%2 !=0:
                mat += int(n//2)
                n = int(n//2) +1
            else:
                mat += int(n/2)
                n = int(n/2)
        return mat