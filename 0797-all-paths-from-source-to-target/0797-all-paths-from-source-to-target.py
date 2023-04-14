class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)-1
        ans = []
        
        def dfs(node, path):
            if node == n:
                ans.append(path[:])
                
            for adj in graph[node]:
                dfs(adj, path + [adj])
                    
        dfs(0, [0])
        return ans