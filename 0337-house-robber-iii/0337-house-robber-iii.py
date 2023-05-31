# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        dp = {}
        def dfs(node):
            if not node: return 0
            
            if node in dp: return dp[node]
            
            root_val = node.val
            if node.left:
                root_val += dfs(node.left.left)+dfs(node.left.right)
            if node.right:
                root_val += dfs(node.right.right) +dfs(node.right.left)
                
            notake = dfs(node.left) + dfs(node.right)
            
            maximum = max(notake, root_val)
            dp[node] = maximum
            
            return maximum
        return dfs(root)