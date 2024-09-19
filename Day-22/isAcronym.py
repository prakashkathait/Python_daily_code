class Solution(object):
    def isAcronym(self, words, s):
        #empty list
        #loop where first letter from each element is added in list 
        #join elements to form a string 
        #finally compare with the s 
        res = []
        for word in words:
            w=word[0][0]
            res.append(w)
        if ''.join(res) == s:
            return True
        else:
            return False