# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def Traverse(parent):
            if not parent:
                return [0, True]
            
            level_left, isBalanced_left = Traverse(parent.left)
            level_right, isBalanced_right = Traverse(parent.right)
            
            if isBalanced_left and isBalanced_right:
                diff = abs(level_left - level_right)
                if diff>1:
                    return [max(level_left, level_right) +1, False]
                else:
                    return [max(level_left, level_right) +1, True]
            
            return [max(level_left, level_right), False]
        return Traverse(root)[1]
            