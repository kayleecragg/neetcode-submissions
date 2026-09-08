class Solution {
public:
    // void recurse(int i, 
    // vector<int>&nums, 
    // vector<int>&curSet, 
    // vector<int>&subsets);

    vector<vector<int>> res;

    vector<vector<int>> subsets(vector<int>& nums) {
        
        vector<int> curSet; 

        recurse(0, nums, curSet);
        return res;
        
    }

    void recurse(int n, 
    vector<int>&nums, 
    vector<int>&curSet) {

        res.push_back(curSet);
        for (auto i = n; i < nums.size(); i++) {
            curSet.push_back(nums[i]);
            recurse(i + 1, nums, curSet);
            curSet.pop_back();
        }
    }
};