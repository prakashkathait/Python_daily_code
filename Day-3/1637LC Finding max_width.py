class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        #sorting list items x-coordinates only 
        x_cor = [point[0] for point in points]
        x_cor.sort()
        #calculate max width 
        max_width = 0
        for i in range(1,len(x_cor)):
            max_width = max(max_width,x_cor[i]-x_cor[i-1])
        return max_width