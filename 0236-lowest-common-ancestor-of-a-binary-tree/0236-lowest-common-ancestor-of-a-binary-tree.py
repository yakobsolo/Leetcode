# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if root.val == p.val or root.val == q.val:
            return root
        if not root.left and not root.right:
            return None
        l, r = None, None
        if root.left:
            
            l = self.lowestCommonAncestor(root.left, p, q)
        if root.right:
            
            r = self.lowestCommonAncestor(root.right, p, q)
        if l!=None and r!=None:
            return root
        
        return  l if l!=None else r
        