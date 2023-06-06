# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        def preorderTraverse(val, node):
            
            if not node: return 
            
            if val < node.val:
                preorderTraverse(val, node.left)
                if not node.left:
                    node.left=TreeNode(val)
                
            else: 
                preorderTraverse(val, node.right)
                if not node.right:
                    node.right = TreeNode(val)
        n = len(preorder)   
        for i in range(1, n):
            preorderTraverse(preorder[i], root)
        return root
        