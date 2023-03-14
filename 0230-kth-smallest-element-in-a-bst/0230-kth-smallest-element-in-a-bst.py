# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = []
        
        def Traverse(root):
            if not root:
                return 
            
            Traverse(root.left)
            ans.append(root.val)
            Traverse(root.right)
        Traverse(root)
        return ans[k-1]
    
    
    
#         ans = []
#         right = 0
#         def Traverse(root):
#             if not root:
#                 return 0
            
#             left = 1 + Traverse(root.left)
#             # sm = left+1
#             if left  == k:
#                 ans.append(root.val)
#                 return 
#             right = Traverse(root.right)
        
            
#             return left
#         Traverse(root)
        
#         return ans[0]