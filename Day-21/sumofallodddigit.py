class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        n = len(arr)
        total_sum = 0 
        i = 0
        for i in range(n):
            contr = ((i+1)*(n-i)+1)//2
            total_sum += contr*arr[i]
        return total_sum