class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        cnt =0
        for s in stones:
            for r in s:
                if r in jewels:
                    cnt +=1
        return cnt