class Solution:
    def rob(self, nums: List[int]) -> int:
        path1, path2 = 0, 0
        for num in nums:
            path1, path2 = path2, max(num + path1, path2)
        return path2
        