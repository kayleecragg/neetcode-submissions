class Solution {
public:
    int rob(vector<int>& nums) {

        vector<int> dp = {0, 0};
        int i = 0;

        while (i < nums.size()) {
            int tmp = max(nums[i] + dp[0], dp[1]);
            dp[0] = dp[1];
            dp[1] = tmp;
            i++;
        }
        return dp[1];
        
    }
};
