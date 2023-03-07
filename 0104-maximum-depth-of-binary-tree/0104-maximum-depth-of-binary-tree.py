# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        
     
        def inorderTraverse( parent):
            
            if not parent:
                return 0
            
            left = inorderTraverse(parent.left)
            right = inorderTraverse(parent.right)
            
            return max(left, right) +1
            
        return inorderTraverse(root)
        