# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hashmap = { v:i for i, v in enumerate(inorder)}
        preorder = deque(preorder)
        def checker(l, r):
            if l>r: return None
            
            val = preorder.popleft()
            
            root= TreeNode(val)
            indx = hashmap[val]
            
            root.left = checker(l, indx-1)
            root.right = checker(indx+1, r)
            
            return root
        return checker(0, len(inorder)-1)
            
            