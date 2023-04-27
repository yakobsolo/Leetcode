# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        q.append(root)
        ans = []
        if root: 
            ans.append([root.val])
        else: return []
        
        while q:
            
            q_len = len(q)
            temp = []
            for i in range(q_len):
                
                if q[0].left:
                    q.append(q[0].left)
                    temp.append(q[0].left.val)

                if q[0].right:
                    q.append(q[0].right)
                    temp.append(q[0].right.val)
                q.popleft()
            if temp: ans.append(temp)
        return ans