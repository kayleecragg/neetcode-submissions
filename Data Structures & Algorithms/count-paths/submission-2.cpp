class Solution {
public:
    int uniquePaths(int m, int n) {
        
        vector<int> prevRow(n, 0);

        for (int r = m - 1; r >= 0; r--) {

            vector<int> curRow(n, 0);
            curRow[n - 1] = 1;

            for (int c = n - 2; c >= 0; c--) {
                curRow[c] = curRow[c + 1] + prevRow[c];
            }
            prevRow = curRow;
        }

        return prevRow[0];

    }
};
