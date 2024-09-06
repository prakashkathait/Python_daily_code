class Solution(object):
    def finalPositionOfSnake(self, n, commands):
        i,j=0,0
        d={
            "UP":(-1,0),
            "DOWN":(1,0),
            "LEFT":(0,-1),
            "RIGHT":(0,1)
        }
        for c in commands:
            a,b=d[c]
            i+=a
            j+=b
        return i*n+j

        
       
        