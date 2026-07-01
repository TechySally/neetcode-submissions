class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
    #understand
    #input: array:int
    #output: true if duplicated, false if not
    #edge cases: empty, one element

    #plan
    #create the function
        #create an empty set
        #loop through list:
            #if num is in set:
                #return true
            #else:
                #add num to the set
        #return false

        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False
