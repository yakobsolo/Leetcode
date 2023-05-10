class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = collections.defaultdict(list)
        indegree = [0] * (n)
        ans = [set() for i in range(n)]
        
        for p, c in edges:
            graph[p].append(c)
            indegree[c] +=1
         
        q = deque()
           
        for i in range(n):
            if not indegree[i]:
                q.append(i)
                
        def bfs():
            
            while q:
                top = q.popleft()
                
                for adj in graph[top]:
                    indegree[adj] -=1
                    ans[adj].update(ans[top])
                    ans[adj].add(top)
                    if indegree[adj] == 0:
                        q.append(adj)
        
        
        
        bfs()
        res = []
        for i, a in enumerate(ans):
            ans[i] = sorted(list(a))
            
        return ans