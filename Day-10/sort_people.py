class Solution(object):
    def sortPeople(self, names, heights):
        #step 1: Pairing names with their corresponding heights 
        paired = [(names[i],heights[i]) for i in range(len(names))]

        #step2: sorting the pairs based on heights in descending order
        paired.sort(key=lambda x:x[1],reverse=True)

        #step3: Extracting sorted names from the sorted pairs 
        sorted_names = [name for name, _ in paired]

        return sorted_names