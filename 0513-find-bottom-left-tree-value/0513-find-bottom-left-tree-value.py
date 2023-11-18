# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        hash  = defaultdict(list)
        def find(node, depth):
            if not node:
                return 0
            hash[depth].append(node.val)
            left = find(node.left, depth+1)+1
            right = find(node.right, depth+1)+1
            return max(left, right)
        mxdepth  = find(root, 1)
        return hash[mxdepth][0]
        
        
        