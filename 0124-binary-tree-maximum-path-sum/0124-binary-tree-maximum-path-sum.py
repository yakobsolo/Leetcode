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
            if left < 0 and right < 0:
                self.max_sum = max(self.max_sum, node.val)
                return int(node.val)
            elif left< 0 and right>=0:
                self.max_sum = max(self.max_sum, node.val + right)
                return int(node.val+right)
            elif right<0 and left>= 0:
                self.max_sum = max(self.max_sum, node.val + left)
                return int(node.val+left)
            else:
                temp = left+right+node.val
                self.max_sum = max(self.max_sum, temp)
                return max(left, right)+node.val
                
            
        dfs(root)
        return self.max_sum