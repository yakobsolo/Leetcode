# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        hash = defaultdict(list)
        def vertical(root, row, col):
            if not root:
                return
            
            hash[col].append([row, root.val])
            vertical(root.left, row+1, col-1)
            vertical(root.right, row+1, col+1)
            
        vertical(root, 0, 0)
        ans = []
        hash = sorted(hash.items(), key=lambda x: x[0] )
        hash = dict(hash)
        for values in hash.values():
            values.sort()
            lis = []
            for i in range(len(values)):
                lis.append(values[i][1])
            ans.append(lis)
        return ans
            
             