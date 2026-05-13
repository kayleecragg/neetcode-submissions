class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        streak, biggeststreak = 0, 0

        for i in range(len(nums)):
            if (nums[i] == 1):
                streak+=1
            else:
                biggeststreak = max(streak, biggeststreak)
                streak = 0
                
        biggeststreak = max(streak, biggeststreak)
        return biggeststreak
            
        