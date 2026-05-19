class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int biggestStreak = 0;
        int streak = 0;

        for (auto num : nums) {
            if (num == 1) {
                streak++;
            }

            else {
                biggestStreak = max(streak, biggestStreak);
                streak = 0;
            }
        }
        biggestStreak = max(streak, biggestStreak);
        return biggestStreak;
    }
};