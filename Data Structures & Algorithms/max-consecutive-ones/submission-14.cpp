class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int max_ones = 0, ones = 0;

        for (auto i : nums) {
            if (i == 1) {
                ones++;
                max_ones = max(max_ones, ones);
                continue;
            }
            ones = 0;
        }
        max_ones = max(max_ones, ones);
        return max_ones;

    }
};