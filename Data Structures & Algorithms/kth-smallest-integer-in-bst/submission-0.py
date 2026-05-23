# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        # gives u root
        # and gives u k

        def dfs(root) -> int | None:
            if not root:
                return None
            
            left = dfs(root.left)
            if left:
                return left
            
            nonlocal k
            k -= 1
            if k == 0:
                return root.val

            right = dfs(root.right)
            if right:
                return right
        
        return dfs(root)
