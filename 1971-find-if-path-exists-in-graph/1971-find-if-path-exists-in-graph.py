class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        
        leng = len(edges)
        for i in range(leng):
            graph[edges[i][0]].append(edges[i][1])
            graph[edges[i][1]].append(edges[i][0])
        traversed = set()  
        
        def dfs(node):
            if node == destination:
                return True
            
            traversed.add(node)
            print(node)
            for neighbor in graph[node]:
                if neighbor not in traversed:
                    if dfs(neighbor):
                        return True
                
        return dfs(source)
         
                
        