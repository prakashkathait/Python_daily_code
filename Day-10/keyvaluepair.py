class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        keys = {'type':0,'color':1,'name':2}
        c = 0
        index = keys[ruleKey]
        for i in items:
            if i[index] == ruleValue:
                c +=1
        return c