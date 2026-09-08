class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        subsets, cur = [], []

        def recurse(i):
            if i >= len(nums):
                subsets.append(cur.copy())
                return

            # include
            cur.append(nums[i])
            recurse(i + 1)
            cur.pop()
    

            # dont include
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            recurse(i + 1)

        recurse(0)
        return subsets

