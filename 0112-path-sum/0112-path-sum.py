# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def path(parent, val):
            if not parent:
                return False
            if not parent.left and not parent.right:
                ans = val + parent.val
                if ans == targetSum:
                    return True
                else:
                    return False
            
            left = path(parent.left, val + parent.val)
            if left:
                return True
            right = path(parent.right, val + parent.val)
            
            return left or right
        return path(root, 0)
            
            
            