class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        import collections 
        graph = collections.defaultdict(list)
        
        n = len(bombs)
        for i in range(n):
            x, y, r= bombs[i]
            
            for j in range(n):
                if i != j:
                    a, b, z = bombs[j]
                    c = (x-a) ** 2 + (y-b)**2
                    if r**2 >= c:
                        graph[i].append(j)
                        
        def dfs(point, visted):
            
            count = 0
            visted.add(point)
            for adj in graph[point]:
                if adj not in visted:
                    count += dfs(adj, visted)
            return count+1
            
            
        ans = 0
        for i in range(n):
            visted = set()
            ans = max(ans, dfs(i, visted))
        return ans