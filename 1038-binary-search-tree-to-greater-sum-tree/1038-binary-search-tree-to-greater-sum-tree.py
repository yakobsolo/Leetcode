# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    tot = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        if not root: return 0
        self.bstToGst(root.right)
        self.tot += root.val
        root.val  = self.tot
        self.bstToGst(root.left)
        
        return root