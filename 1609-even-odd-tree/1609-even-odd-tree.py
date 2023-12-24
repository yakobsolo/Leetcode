# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        level = defaultdict(list)
        
        def levelorder(node, idx):
            if not node: return True
            
            if idx in level:
                if idx%2 == 0:
                    if node.val%2 ==1 and level[idx][-1] < node.val:
                        level[idx].append(node.val)
                        
                    else:
                        return False
                else:
                    if node.val%2 == 0 and level[idx][-1] > node.val:
                        level[idx].append(node.val)
                    else:
                        return False
            else:
                if idx%2== 0 and node.val%2 == 1:
                    level[idx].append(node.val)
                elif idx%2 == 1 and node.val%2 == 0:
                    level[idx].append(node.val)
                    
                else:
                    return False
                level[idx].append(node.val)
            
            
            left = levelorder(node.left, idx+1)
            right = levelorder(node.right, idx+1)
            
            return left&right
        
        return levelorder(root, 0)