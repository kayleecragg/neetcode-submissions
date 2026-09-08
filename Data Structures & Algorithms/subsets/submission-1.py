class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets, curSet = [], []
        Solution.helper(0, nums, curSet, subsets)
        return subsets
    
    @staticmethod
    def helper(i, nums, curSet, subsets):
        if i>= len(nums):
            subsets.append(curSet.copy())
            return

        # include
        curSet.append(nums[i])
        Solution.helper(i + 1, nums, curSet, subsets)
        curSet.pop()

        # dont include
        Solution.helper(i + 1, nums, curSet, subsets)