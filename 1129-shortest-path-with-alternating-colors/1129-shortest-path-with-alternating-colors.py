class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        
        
            
        graph = collections.defaultdict(list)
        ans = [-1]*n
        ans[0] = 0
        
        for p, c in redEdges:
            graph[p].append((c, "r"))
        for p, c in blueEdges:
            graph[p].append((c, "b"))
        
        visted = []
        q = collections.deque()
        q.append([0, "r"])    
        q.append([0, "b"])
        dis = 1
        def bfs():
            nonlocal dis
            visted = set()
            while q:
                
                q_len= len(q)
               
                for i in range(q_len):
                    p, p_color = q.popleft()
                    
                    
                    
                    for child in graph[p]:
                        c,c_color = child
                        
                        if (c, c_color) not in visted:
                            if p_color != c_color:
                                visted.add((c, c_color))
                                q.append([c, c_color])
                                if ans[c] == -1:
                                    
                                    ans[c] = dis
                dis +=1
                   
            
        bfs()
        return ans
        