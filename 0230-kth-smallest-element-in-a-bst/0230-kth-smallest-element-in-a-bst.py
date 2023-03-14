# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

    
        count = 0
        ans = []
        def Traverse(root):
            nonlocal count
            if not root or ans:
                return 
            
            Traverse(root.left)
            count +=1
        
            if count == k:
                
                ans.append(root.val)
                return 
            Traverse(root.right)
        Traverse(root)
        
        return ans[0]
           