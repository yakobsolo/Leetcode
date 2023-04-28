# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = -inf
        
        def dfs(node):
            if not node: return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            temp = left + right +node.val
            temp2 = left + node.val
            temp3 = right + node.val
            self.max_sum = max(temp, temp2, temp3, node.val, self.max_sum)
            
            return max(temp2, temp3, 0)
            
            
            
           
        dfs(root)
        return self.max_sum