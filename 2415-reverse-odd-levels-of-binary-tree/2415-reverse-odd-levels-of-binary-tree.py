# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def traverse(node1,node2,  lev):
            if not node1 or not node2: return 
            
            
            if lev%2 == 1:
                node1.val, node2.val = node2.val, node1.val
                
            traverse(node1.left, node2.right, lev+1)
            traverse(node1.right, node2.left, lev+1)
            
        traverse(root.left, root.right, 1)
        return root
            
            