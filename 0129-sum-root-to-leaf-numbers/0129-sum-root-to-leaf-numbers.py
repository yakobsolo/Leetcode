# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = []
        def dfs(node, path):
            if not node:
                return 
            if not node.left and not node.right:
                ans.append(path+[str(node.val)])
                return
            dfs(node.left, path+[str(node.val)])
            dfs(node.right, path+[str(node.val)])
            
        dfs(root, [])
        tot = 0
        for path in ans:
            tot += int("".join(path))
        return tot