class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        color = [0]*len(graph)
        done = set()
        inprocess = set()
        ans = []
        
        def dfs(n):
            if color[n] == 2: return True
            if color[n] ==1: return False
            
            color[n] = 1
            res = True
            for adj in graph[n]:
                res &= dfs(adj)
            
            if res:
                color[n] = 2
                ans.append(n)
                return True
            return False
            
            
        for i in range(len(graph)):
            if color[i] != 1 and color[i] != 2:
                dfs(i)
        return sorted(ans)
        