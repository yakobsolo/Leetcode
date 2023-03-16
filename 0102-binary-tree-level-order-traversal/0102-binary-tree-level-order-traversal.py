# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        hash = {}
        
        def level(root, lev):
            if not root:
                return 
            hash.setdefault(lev, []).append(root.val)
            level(root.left, lev +1)
            
            
            level(root.right, lev+1)
        level(root, 1)
        
        lis = []
        for key in hash:
            lis.append(hash[key])
        
        return lis