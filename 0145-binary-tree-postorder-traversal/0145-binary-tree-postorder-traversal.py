# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        
        def postorderTraverse( parent):
            if not parent:
                return
            postorderTraverse(parent.left)
            postorderTraverse(parent.right)
            ans.append(parent.val)

            
        postorderTraverse(root)
        return ans