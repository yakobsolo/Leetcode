# code here
        graph=collections.defaultdict(list)
        indegree=[0] * (n+1)
        
        for u,v in edges:
            graph[u].append(v)
            indegree[v]+=1
        q=collections.deque()
        for i in range(1,n+1):
            if indegree[i]==0:
                q.append(i)
        ans=[]
        lev=1
        
        ans = [0]*n
        while q:
            q_len=len(q)
            for _ in range(q_len):
                
                top=q.popleft()
                ans[top-1] = lev
                for adj in graph[top]:
                    indegree[adj]-=1
                    if indegree[adj]==0:
                        q.append(adj)
            lev+=1
            
        
        
        return " ".join(map(str,ans))
            
