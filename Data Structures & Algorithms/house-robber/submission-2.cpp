class Solution {
public:
    int rob(vector<int>& nums) {

        // // base case
        // if (n < 3) return n; 

        vector<int> dp = {0, 0};
        int i = 0, n = nums.size();

        while (i < n) {
            int tmp = max(nums[i] + dp[0], dp[1]);
            dp[0] = dp[1];
            dp[1] = tmp;
            i++;
        }
        return dp[1];
        
    }
};
