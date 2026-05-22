# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # helper function to find minimum node
    def findMinNode(self, root) -> Optional[TreeNode]:

        curr = root
        while curr and curr.left:
            curr = curr.left

        return curr

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if not root:
            return None

        # search for node you want to delete

        # if the curr node is bigger than the value you want to delete, go left!
        if key > root.val:
            root.right = self.deleteNode(root.right, key)

        # if the curr node is smaller than the value you want to delete, go right!
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)

        else:
            if not root:
                return None

            # case 1: no children / 1 child node
            if not root.left:
                return root.right

            elif not root.right:
                return root.left

            # case 2: 2 child nodes
            else:
                minNode = self.findMinNode(root.right)
                root.val = minNode.val
                root.right = self.deleteNode(root.right, minNode.val)

        return root