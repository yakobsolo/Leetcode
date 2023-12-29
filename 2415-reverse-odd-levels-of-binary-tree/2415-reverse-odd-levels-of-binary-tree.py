# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        hash = defaultdict(list)
        def traverse(node, lev):
            
            if not node: return
            
            
            if lev%2 == 1:
                hash[lev].append(node.val)
                
            traverse(node.left, lev+1)
            traverse(node.right, lev+1)
        
        traverse(root, 0)
        
        
        def insert(node, lev):
            if not node: return
            
            if lev%2 == 1:
                node.val = hash[lev].pop()
            insert(node.left, lev+1)
            insert(node.right, lev+1)
        insert(root, 0)
        return root