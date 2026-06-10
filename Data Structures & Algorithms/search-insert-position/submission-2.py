class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        lo = 0 
        hi = len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            if target == nums[mid]:
                return mid
            
            elif target < nums[mid]:
                hi = mid -1
            
            elif target > nums[mid]:
                lo = mid + 1
        
        # if its here means target not found
        
        for i in range(len(nums)):
            # if there is a bigger number than target, this is the place to insert it
            if nums[i] >= target:
                return i
            # if target is the largest number in the array
            elif i == len(nums) - 1:
                return i + 1