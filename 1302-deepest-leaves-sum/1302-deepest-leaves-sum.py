# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        hash, mx = defaultdict(int), 0
        def find(node, depth):
            nonlocal mx
            if not node: return 
            if not node.left and not node.right:
                hash[depth]+=node.val
                return
            mx = max(mx, depth+1)
            l= find(node.left, depth+1)
            r = find(node.right, depth+1)
        find(root, 0)
        return hash[mx]