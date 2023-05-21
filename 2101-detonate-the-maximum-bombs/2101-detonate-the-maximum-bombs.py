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
                        
        def bfs(point):
            q = collections.deque()
            visted = set()
            
            q.append(point)
            
            
            while q:
                q_len = len(q)
                visted.add(point)
                
                for i in range(q_len):
                    top = q.popleft()
                    visted.add(top)
                    for adj in graph[top]:
                        if adj not in visted:
                            q.append(adj)
            return len(visted)
            
        ans = 0
        for i in range(n):
            ans = max(ans, bfs(i))
        return ans