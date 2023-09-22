class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        
        
        
        queue = deque()
        ans = [-1]*n
        lev = 1
        
        visted = set()
        graph = defaultdict(list)
        
        for p, c in redEdges:
            graph[p].append((c, "r"))
        for p, c in blueEdges:
            graph[p].append((c, "b"))
        
        queue.append((0, "r"))
        queue.append((0, "b"))
        ans[0] = 0
        while queue:
            
            q_len= len(queue)
            
            for _ in range(q_len):
                p, p_color = queue.popleft()
                
                for c, c_color in graph[p]:
                    if (c, c_color) not in visted:
                        
                        if p_color != c_color:
                            visted.add((c, c_color))
                            queue.append((c, c_color))

                            if ans[c] == -1:
                                ans[c] = lev
                            
            lev+=1
        return ans
            
            

            
        
        
        
                            
                            
                            
                        
                            
                            
        
                            
                            
                            
                            