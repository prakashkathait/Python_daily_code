class Solution(object):
    def canFormArray(self, arr, pieces):
        #create a dictionary to map the first element of each subarray to the subarray
        piece_map = {piece[0]:piece for piece in pieces}

        i=0
        while i <len(arr):
            #check if the current element in arr matches any subarray in pieces
            if arr[i] in piece_map:
                piece = piece_map[arr[i]]
                #check if the subarray matches the corresponding element in arr
                if arr[i:i+len(piece)] ==piece:
                    i += len(piece)
                else:
                    return False
            else:
                return False 
        return True