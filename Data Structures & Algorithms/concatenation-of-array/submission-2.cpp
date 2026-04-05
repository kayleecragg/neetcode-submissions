class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {

        int size = (int)nums.size();
        vector<int> ans(size * 2);

        int j = 0;
        for (auto i = 0; i < (int)ans.size(); i++) {
            if (i < size) {
                ans[i] = nums[i];
            }
            else {
               ans[i] = nums[j++]; 
            }
        }

        return ans;
    }
};