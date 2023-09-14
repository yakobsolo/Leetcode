# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        tot = 0
        def bst(root):
            nonlocal tot
            if not root: return 0
            bst(root.right)
            tot += root.val
            root.val  = tot
            bst(root.left)
        bst(root)
        return root