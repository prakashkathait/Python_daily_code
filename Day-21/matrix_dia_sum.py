class Solution(object):
    def diagonalSum(self, mat):
        i = 0
        sum = 0 
        n = len(mat)
        for i in range(n):
            sum += mat[i][i] + mat[i][n-i-1]
        if n%2 == 1:
            sum -= mat[n//2][n//2]
        return sum 