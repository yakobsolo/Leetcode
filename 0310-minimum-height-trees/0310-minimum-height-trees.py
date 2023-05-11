class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n== 1:
            return [0]
        graph=defaultdict(list)
        indegree = [0] *n 
        for p, c in edges:
            graph[p].append(c)
            graph[c].append(p)
            indegree[p] +=1
            indegree[c] +=1
        
        q = deque()
        for i in range(n):
            if indegree[i] == 1: q.append(i)
         
        ans = []
        def bfs():
            done = set()
            while q:
                nextprocess = set()
                q_len =len(q)
                
                for _ in range(q_len):
                
                    top = q.popleft()
                    done.add(top)
                   
                    for adj in graph[top]:
                        if adj in q:
                            ans.append(top)
                            ans.append(adj)
                            return
                        
                        if adj not in done:
                            indegree[adj] -=1
                            if indegree[adj] == 0:
                                ans.append(adj)
                                return 
                            if indegree[adj] == 1:
                                nextprocess.add(adj)
                                
                for next in nextprocess:
                    q.append(next)
                 

        bfs()
        return ans