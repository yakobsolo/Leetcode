# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        hash = defaultdict(list)
        def level(root, lev, node):
            if not root:
                return
            
            hash[lev].append(node)
            level(root.left, lev +1, 2*node)
            level(root.right,lev +1, 2*node+1)
            
        level(root, 1, 1)
        maxwidth = 0
        for values in hash.values():
            
            maxwidth = max(maxwidth, values[-1] - values[0] +1)
            
        return maxwidth
        
        