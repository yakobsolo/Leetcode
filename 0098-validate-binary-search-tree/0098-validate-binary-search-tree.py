# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        mx = -inf
        def binarysearch(parent):
            nonlocal mx
            if not parent:
                return True
        
            left = binarysearch(parent.left)
            if mx < parent.val:
                mx = parent.val
            else:
                return False
            right= binarysearch(parent.right)
            return left and right
        return binarysearch(root)
        
        