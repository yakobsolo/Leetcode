# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        hash = Counter()
        
        def mode(parent):
            if not parent:
                return 
            
            hash[parent.val] += 1
            mode(parent.left)
            mode(parent.right)
        
        mode(root)
        
        modes = sorted(hash.items(), key = lambda x: x[1], reverse=True)
        mod = modes[0]
        ans = []
        ans.append(mod[0])
        for i in range(1, len(modes)):
            
            if modes[i][1] == mod[1]:
                ans.append(modes[i][0])
        return ans
                
       
        
        