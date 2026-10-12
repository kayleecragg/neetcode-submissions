class Solution {
public:
    int climbStairs(int n) {
        // base case
        if (n < 3) return n;
        
        vector<long long> dp = {1, 1};
        int i = 1;

        while (i <= n) {
            long long tmp = dp[1];
            dp[1] = dp[0] + dp[1];
            dp[0] = tmp;
            i++;
        }
        return dp[0];
    }
};
