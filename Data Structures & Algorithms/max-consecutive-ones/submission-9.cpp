class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {

        int bigstreak = 0;
        int streak = 0;

        for (auto i : nums) {
            if (i == 1) {
                streak++;
                if (streak >= bigstreak) {
                    bigstreak = streak;
                }
            }
            else {
                streak = 0;
            }
        }

        if (streak >= bigstreak) {
            bigstreak = streak;
        }

        return bigstreak;
        
    }
};