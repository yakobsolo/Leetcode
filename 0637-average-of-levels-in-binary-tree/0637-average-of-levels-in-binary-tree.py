# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans= []
        queue = deque()
        queue.append(root)
        while queue:
            cur_lev_len = len(queue)
            tot = 0
            
            for i in range(cur_lev_len):
                child = queue.popleft()
                tot += child.val
                if child.left: 
                    queue.append(child.left)
                if child.right:
                    queue.append(child.right)
            
            ans.append(tot/cur_lev_len)
        return ans
            