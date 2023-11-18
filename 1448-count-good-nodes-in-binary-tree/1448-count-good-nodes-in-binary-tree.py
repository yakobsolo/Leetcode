# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        
        def find(node, prevmx):
            nonlocal ans
            if not node:
                return
            
            if node.val >= prevmx:
                ans+=1
            
            find(node.left, max(node.val, prevmx))
            find(node.right, max(node.val, prevmx))
            
        find(root, root.val)
        return ans
            