/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool findTargetPath(TreeNode* root, std::vector<int>&nums, int targetSum) {

        if (!root) {
            return false;
        }

        nums.push_back(root->val);

        if (!root->left && !root->right) {
            auto maybesum = 0;
            for (auto num : nums) {
                maybesum +=num;
            }
            if (maybesum == targetSum) {
                return true;
            }
        }

        if (findTargetPath(root->left, nums, targetSum)) return true;
        if (findTargetPath(root->right, nums, targetSum)) return true;

        nums.pop_back();
        return false;

    }

    bool hasPathSum(TreeNode* root, int targetSum) {
        std::vector<int> nums;
        return findTargetPath(root, nums, targetSum);
    }
};