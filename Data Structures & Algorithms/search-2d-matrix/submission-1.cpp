class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int rows = (int)matrix.size(), cols = (int)matrix[0].size();
        int lo = 0, hi = (rows * cols) - 1;

        while (lo <= hi) {
            int mid = (lo + hi) / 2;

            int r = mid / cols, c = mid % cols;
            if (target > matrix[r][c]) {
                lo = mid + 1;
            }
            else if (target < matrix[r][c]) {
                hi = mid - 1;
            }
            else {
                return true;
            }
        }
        return false;
    }
};
