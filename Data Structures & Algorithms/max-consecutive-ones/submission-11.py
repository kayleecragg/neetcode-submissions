class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        streak, biggeststreak = 0, 0

        for num in nums:
            if (num == 1):
                streak+=1
            else:
                biggeststreak = max(streak, biggeststreak)
                streak = 0

        biggeststreak = max(streak, biggeststreak)
        return biggeststreak
            
        