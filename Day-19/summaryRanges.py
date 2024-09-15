class Solution(object):
    def summaryRanges(self, nums):
        # If nums is empty, return an empty list immediately.
        if not nums:
            return []
        
        # Initialize an empty result list to store the ranges.
        res = []
        
        # Start and end both point to the first element, since we are processing the first range.
        start, end = nums[0], nums[0]
        
        # Iterate over the array starting from the second element.
        for i in range(1, len(nums)):
            # If the current number is greater than end + 1, it means there's a gap (non-consecutive numbers).
            if nums[i] > end + 1:
                # If start and end are different, we have a range, so add it as "start->end".
                if start != end:
                    res.append(str(start) + "->" + str(end))
                else:
                    # If start == end, it's a single number, so add it as "end".
                    res.append(str(end))
                
                # Move the start and end pointers to the new number since the current range ended.
                start, end = nums[i], nums[i]
            else:
                # If nums[i] is consecutive (nums[i] == end + 1), update end to extend the range.
                end = nums[i]
        
        # After the loop, we need to add the last processed range to the result.
        if start != end:
            res.append(str(start) + "->" + str(end))
        else:
            res.append(str(end))
        
        # Return the list of ranges.
        return res
