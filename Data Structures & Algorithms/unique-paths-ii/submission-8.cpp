class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {

        int m = obstacleGrid.size();
        int n = obstacleGrid[0].size();

        vector<int> dp(n, 0);
        dp[n - 1] = 1;

        for (int r = m - 1; r >= 0; r--) {
            for (int c = n - 1; c >= 0; c--) {
                // base case
                if (obstacleGrid[r][c]) dp[c] = 0;
                // anything else
                else if (c + 1 < n) dp[c] = dp[c] + dp[c+1];
            }
        }
        return dp[0];
    }
};