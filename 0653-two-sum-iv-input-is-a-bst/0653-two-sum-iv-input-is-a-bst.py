# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        visted = set()
        def traverse(node):
            if not node:
                return False
            diff = k - node.val
            if diff in visted:
                return True
            visted.add(node.val)
            
            left = traverse(node.left)
            right = traverse(node.right)
            
            return left or right
        if traverse(root):
            return True
        return False