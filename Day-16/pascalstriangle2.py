class Solution(object):
    def getRow(self, rowIndex):
        result=[]
        for i in range(rowIndex+1):
            row =[None for x in range(i+1)]
            row[0],row[-1]=1,1
            for j in range(1,len(row)-1):
                row[j]=result[i-1][j-1]+result[i-1][j]
            result.append(row)
        return result[rowIndex]