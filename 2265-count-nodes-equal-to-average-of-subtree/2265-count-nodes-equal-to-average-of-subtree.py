# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def average(parent):
            nonlocal ans
            if not parent:
                return [0, 0]
            
            left, nodesleft = average(parent.left)
            right, nodesright = average(parent.right)
            
            sums = left+right+parent.val
            nodes = nodesleft + nodesright +1
            
            if (sums)//nodes == parent.val:
                ans+=1
            
            return [sums, nodes]
        average(root)
        return ans