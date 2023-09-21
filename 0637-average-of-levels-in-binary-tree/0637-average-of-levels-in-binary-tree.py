# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque()
        
        queue.append(root)
        ans = []
        
        while queue:
            summ = 0
            
            leng = len(queue)
            for _ in range(leng):
                top = queue.popleft()
                summ += top.val
                if top.left:
                    queue.append(top.left)
                if top.right:
                    queue.append(top.right)
            
            ans.append(summ/leng)
            
                
        return ans
            
            