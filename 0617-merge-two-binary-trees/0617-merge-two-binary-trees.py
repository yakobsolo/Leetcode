# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root1 and not root2:
            return 
        
        
        def merge(parent1, parent2):
            
            if not parent1 and not parent2:
                return 
            if not parent1 and parent2:
                        
                return parent2
            elif not parent2 and parent1:
                
                return parent1
            merged = TreeNode(parent1.val+parent2.val)
            
            
                        
            merged.left = merge(parent1.left, parent2.left)
            merged.right = merge(parent1.right, parent2.right)
            return merged
        
        return merge(root1, root2)
        