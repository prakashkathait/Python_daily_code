class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
          # Create hset for storing previous occurrences of the elements in the array...
        dict={}
        #traversing each element with for loop in the array
        # and whether the difference between the current index and its previous index is <= k.
        for i in range(len(nums)):
    # If both conditions are true, return True (i.e., a duplicate within k distance was found)
            if nums[i] in dict and abs(i - dict[nums[i]])<=k:
                return True
    # Update the current element's index in the dictionary hset...
            # This tracks the latest position of each number. 
            dict[nums[i]] = i
    #If no such pair will found will return False
        return False
