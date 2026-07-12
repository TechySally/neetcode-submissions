class Solution:
    def search(self, nums: List[int], target: int) -> int:

       #binary search:
       #find the middle, compare to target
        #if target, return index
       #if not target 
        #if middle is greater than target, search the left
        #if middle is less than target, search the right
        

        #case: odd numbers, even numbers (taken care of with integer division)

        left = 0
        right = len(nums) -1
        
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1

            