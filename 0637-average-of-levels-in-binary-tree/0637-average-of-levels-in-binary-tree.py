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
            temp = deque()
            leng = len(queue)
            for parent in queue:
                summ += parent.val
                if parent.left:
                    temp.append(parent.left)
                if parent.right:
                    temp.append(parent.right)
            
            ans.append(summ/leng)
            queue = deque()
            queue = temp
                
        return ans
            
            