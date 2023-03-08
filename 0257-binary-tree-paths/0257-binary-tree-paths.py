# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans =[]
        
        def Traverse(parent, prev):
            
            if not parent:
                return 
            if not parent.left and not parent.right:
                prev+= str(parent.val)
                ans.append(prev)
                return 
            prev += str(parent.val) + "->"
            Traverse(parent.left, prev)
            Traverse(parent.right, prev)
            
        Traverse(root, "")
        return ans