# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        ans = 0
        
        def longest(node, parent):
            nonlocal ans
            if not node:
                return 0
            
            left = longest(node.left, node.val)
            
            right = longest(node.right,node.val)
            ans = max(ans, left + right)
            if node.val != parent:
                return 0
            else:
                return max(left, right) + 1
        longest(root, -2000)
        return ans