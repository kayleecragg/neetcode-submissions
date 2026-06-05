class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        countMap = {}
        for i in range(len(nums)):           

            res = target - nums[i]
            if res in countMap:
                return [countMap[res], i]
            
            countMap[nums[i]] = i
            
            