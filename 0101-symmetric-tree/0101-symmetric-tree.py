# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        
        
        def rootLeft(parent1, parent2):
            if not parent1 and not parent2:
                return True
            if not parent1 and parent2:
                return False
            if not parent2 and parent1:
                return False
            if parent1.val != parent2.val:
                return False
            
            
            left= rootLeft(parent1.left, parent2.right)
            right = rootLeft(parent1.right, parent2.left)
            return left and right
        return rootLeft(root.left, root.right)
            
            
            
            
           
        
        return rootLeft(root.left, root.right)
            
        
      