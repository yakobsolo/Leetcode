# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level = defaultdict(int)
        # mx = [-inf, 0]
        
        def levelorder(node, lev):
            if not node: return
            
            level[lev] +=node.val
            levelorder(node.left, lev+1)
            levelorder(node.right, lev+1)
        levelorder(root, 1)
        val = []
        for key, v in level.items():
            val.append(v)
        mx  = max(val)
        for i in range(len(val)):
            if val[i] == mx:
                return i+1
       