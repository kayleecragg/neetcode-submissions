class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        biggestStreak, streak = 0, 0

        for i in nums:
            if (i == 1):
                streak += 1
                biggestStreak = max(streak, biggestStreak)
            else:
                streak = 0

        biggestStreak = max(streak, biggestStreak)

        return biggestStreak

        