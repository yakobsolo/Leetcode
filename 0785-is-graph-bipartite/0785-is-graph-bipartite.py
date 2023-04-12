class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        bi = [0]*n
        visted = set()
        def bipartite(node, prev):
            bi[node] = prev
            visted.add(node)
            # print(node, bi)
            # print(visted)
            for neighbor in graph[node]:
                # print(neighbor, node)
                if neighbor not in visted:
                    if bipartite(neighbor, -prev):
                        continue
                    return False
                        
                else:
                    if bi[neighbor] == bi[node]:
                        return False
            return True
        
        for i in range(n):
            if i not in visted and not bipartite(i, 1):
                    return False
            # print(i, bi)
        return True
        
        