# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        llist = []

        def kms(root):        
            if not root:
                return 
            
            root.left = kms(root.left)
            llist.append(root.val)
            root.right = kms(root.right)

        kms(root)
        return llist
        


