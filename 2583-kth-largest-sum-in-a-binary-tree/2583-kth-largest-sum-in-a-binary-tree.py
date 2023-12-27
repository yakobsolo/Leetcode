# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        level = defaultdict(int)
        
        def levelOrder(node, lev):
            if not node: return 
            
            level[lev] += node.val
            levelOrder(node.left, lev+1)
            levelOrder(node.right, lev+1)
            
        levelOrder(root, 0)
        if k> len(level): return -1
        sm = list(level.values())
        sm.sort()
        
        return sm[-k]
            