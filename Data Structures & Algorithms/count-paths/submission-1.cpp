class Solution {
public:
    int uniquePaths(int m, int n) {
        int cols = n;
        int rows = m;
        vector<int> prevRow(cols, 0);

        for (int r = rows - 1; r >= 0; r--) {
            vector<int> curRow(cols, 0);
            curRow[cols - 1] = 1;

            for (int c = cols - 2; c >= 0; c--) {
                curRow[c] = curRow[c + 1] + prevRow[c];
            }
            prevRow = curRow;
        }
        return prevRow[0];
    }
};
