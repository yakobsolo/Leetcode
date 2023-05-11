class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        if len(quiet) == 1:
            return [0]
        
        graph = collections.defaultdict(list)
        indegree = [0] * len(quiet)
        
        for r, p in richer:
            graph[p].append(r)
            indegree[r] +=1
            
        color = [0] * len(quiet)
        
        ans = [-1] * len(quiet)
        
        def dfs(n):
            node = n
            
            for adj in graph[n]:
                if ans[adj] != -1:
                    new_node = ans[adj]
                
                else:
                    new_node = dfs(adj)
                
                if quiet[node] > quiet[new_node]:
                    node = new_node
                
            ans[n] = node
            
            return node
            
        
        for i in range(len(indegree)):
            if indegree[i] == 0:
                dfs(i)
        
        return ans
        
        