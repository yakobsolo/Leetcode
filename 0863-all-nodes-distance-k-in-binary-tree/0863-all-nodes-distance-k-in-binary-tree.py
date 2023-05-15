# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = collections.defaultdict(list)
        
        def traverse(node):
            if not node.left and not node.right:
                return 
            
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                traverse(node.left)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                traverse(node.right)
        traverse(root)        
        
        q = collections.deque()
        q.append(target.val)
        visted, lev = set(), 0
        ans = []
        visted.add(target.val)

        while q and lev<k:
            q_len = len(q)
            for _ in range(q_len):

                top = q.popleft()
                visted.add(top)
                for adj in graph[top]:
                    if adj not in visted:
                        q.append(adj)

            lev +=1
            
        while q:
            ans.append(q.popleft())
        return ans