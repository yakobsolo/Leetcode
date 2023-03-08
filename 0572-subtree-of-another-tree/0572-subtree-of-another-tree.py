# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def Traverse(root, subRoot):
            if not root and not subRoot:
                return True
            if not root and subRoot:
                return False
            if not subRoot and root:
                return False

            if root.val != subRoot.val:
                return False

            left1 = Traverse(root.left, subRoot.left)
            left2 = Traverse(root.right, subRoot.right)

            return left1 and left2
        
        
        def subtree(root, subRoot):
            if not root:
                return 
        
            if root.val == subRoot.val:
                if Traverse(root, subRoot):
                    return True
            
            isleft = subtree(root.left, subRoot)
            isright = subtree(root.right, subRoot)
        
            return isleft or isright
        return subtree(root, subRoot)