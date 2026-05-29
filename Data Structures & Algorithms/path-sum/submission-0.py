# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        targetArr = []

        def checkfortargetsum(root, targetArr, targetSum):
            # base case 1, if root is none return false 
            if not root:    
                return False

            # append val to targetArr
            targetArr.append(root.val)

            # base case 2, if reached leaf node
            # and the sum in the array is equal to targetSum
            if not root.left and not root.right:
                maybe = 0
                for i in targetArr:
                    maybe += i
            
                if maybe == targetSum:
                    return True
                
            # recursively check left and right
            if checkfortargetsum(root.left, targetArr, targetSum):
                return True
            
            if checkfortargetsum(root.right, targetArr, targetSum):
                return True
            
            targetArr.pop()
            return False
        
        return checkfortargetsum(root, targetArr, targetSum)

