class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
    int count = 0;
    // count the number of val occurrences
    for (auto i = 0; i < nums.size(); i++) {
        if (nums[i] == val) {
            count++;
        }
        else {
            nums[i - count] = nums[i]; // shift by number of val occurrences so far
        }
    }
    int k = (int)nums.size() - count;
    return k;  
    }
};