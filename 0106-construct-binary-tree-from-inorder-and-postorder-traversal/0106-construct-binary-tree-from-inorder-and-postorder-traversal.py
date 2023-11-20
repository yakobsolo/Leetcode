# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        hashmap = {v:i for i, v in enumerate(inorder)}
        
        def checker(l, r):
            if l>r: return None
            
            root = TreeNode(postorder.pop())
            index = hashmap[root.val]
            root.right = checker(index+1, r)
            root.left = checker(l, index-1)


            return root
        
        return checker(0, len(inorder)-1)