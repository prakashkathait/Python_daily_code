# LC 1431: Kids with Greatest number of Candies 

class Solution(object):
    def kidsWithCandies(self, candies, extra):
        result =[]
        i=0
        j=0
        maxi=0
        for j in range(0, len(candies)):
            if candies[j] > maxi:
                maxi = candies[j]
        for i in range(0,len(candies)):
            if candies[i] + extra >= maxi:
                result.append(True)
            else:
                result.append(False)
        return result