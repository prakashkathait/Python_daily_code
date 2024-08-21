class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        cnt =0
        for hrs in hours:   
            if hrs >=target:
                cnt +=1
            else: 
                0
        return cnt