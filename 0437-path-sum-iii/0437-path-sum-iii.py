# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        self.count = 0
        
        hashmap = defaultdict(int)
        hashmap[0] = 1
        
        def paths(node, path):
            if not node:
                return 
            
            path +=node.val
            diff = path - targetSum
            if diff in hashmap:
                self.count += hashmap[diff]
            hashmap[path] +=1
            paths(node.left, path)
            paths(node.right, path)
            # print(path)
            hashmap[path] -=1
            
        paths(root, 0)   
        return self.count