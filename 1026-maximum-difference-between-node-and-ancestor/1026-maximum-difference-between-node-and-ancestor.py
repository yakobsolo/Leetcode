# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = 0
        
        def find(node):
            nonlocal ans
            
            if node.left:
                left = find(node.left)
            else:
                left = [node.val, node.val]
            if node.right:
                right = find(node.right)
            else: right = [node.val, node.val]
            
            ans = max(ans, abs(min(left[0], right[0]) - node.val), abs( max(left[1], right[1])-node.val))
            return [min(left[0], right[0], node.val), max(left[1], right[1], node.val)]
        find(root)
        return ans