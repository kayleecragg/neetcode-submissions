class Solution {
public:
    int search(vector<int>& nums, int target) {
        
        auto lo = 0; 
        auto hi = (int)nums.size() - 1;

        while (lo <= hi){
            auto mid = (hi + lo) / 2;
            if (target < nums[mid]) {
                hi = mid - 1;
            }
            else if (target > nums[mid]) {
                lo = mid + 1;
            }
            else {
                return mid;
            }
        }

        return -1;
    }
};