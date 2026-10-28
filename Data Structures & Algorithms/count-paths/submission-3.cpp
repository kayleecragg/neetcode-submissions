class Solution {
public:
    int uniquePaths(int m, int n) {
        
        vector<int> prevRow(n, 0);

        for (int i = m - 1; i >= 0; i--) {
            vector<int> curRow(n, 0);
            curRow[n - 1] = 1;
            for (int j = n - 2; j >= 0; j--) {
                curRow[j] = curRow[j + 1] + prevRow[j];
            }
            prevRow = curRow;
        }
        return prevRow[0];
    }
};
