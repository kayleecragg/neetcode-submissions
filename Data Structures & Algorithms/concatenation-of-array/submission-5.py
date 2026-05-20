class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        x = len(nums) * 2
        ans = [0] * x

        for i in range(len(nums)):
            ans[i] = nums[i]
            ans[i + n] = nums[i]

        return ans