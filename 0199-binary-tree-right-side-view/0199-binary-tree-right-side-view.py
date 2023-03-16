# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        hash = defaultdict(int)
        def level(root, lev):
            if not root:
                return 
            
            hash[lev] =root.val
            level(root.left, lev +1)
            
            
            level(root.right, lev+1)
        level(root, 1)
        
        return hash.values()
        
        # for key in hash:
        #     lis.append(hash[key][-1])
        # return lis