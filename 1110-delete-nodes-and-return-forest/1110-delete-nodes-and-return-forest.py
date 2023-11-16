# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        def dfs(node):
            if not node: return None
            
            node.left, node.right = dfs(node.left), dfs(node.right)
            
            if node.val in to_delete:
                if node.left:
                    ans.append(node.left)
                if node.right:
                    ans.append(node.right)
                return None
            else:
                return node
        ans = []
        node = dfs(root)
        if node:
            ans.append(node)
        return ans
        
                    