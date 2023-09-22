# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        queue.append(root)
        ans = []
        if not root: return []
        while queue:
            
            leng = len(queue)
            temp = []
            for _ in range(leng):
                top = queue.popleft()
                if top:
                    temp.append(top.val)
                if top.left: queue.append(top.left)
                if top.right: queue.append(top.right)
            ans.append(temp)
        return ans