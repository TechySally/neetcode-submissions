class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #create function
            #create empty dictionary (seen)
            #loop through the array with enumerate() so you can see both index and value
            #calculate complement: target - number
            #if the complement is in the dicitonary, you found the pair
                #if its not there, add the number and index to dictionary
        
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement],i ]
            
            seen[num] = i

        
