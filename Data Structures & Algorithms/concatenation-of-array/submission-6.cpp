class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        int n = nums.size();
        vector<int> returnthing;
        returnthing.resize(2 * n);

        for (int i = 0; i < n; i++) {
            returnthing[i] = nums[i];
            returnthing[i + n] = nums[i];
        }

        return returnthing;
    }
};