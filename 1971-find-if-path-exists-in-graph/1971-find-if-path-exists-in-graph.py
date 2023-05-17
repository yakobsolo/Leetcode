class Solution:
        
    
        
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        root = [i for i in range(n)]
        rank = [1 for _ in range(n)]

        def find(node):
            if root[node] == node:
                return node
            root[node] = find(root[node])
            return root[node]
        
        
        def union(x, y):
            
            par1 = find(x)
            par2 = find(y)
            if par1 != par2:
                if rank[par1] > rank[par2]:
                    root[par2] = par1
                    rank[par1] += 1
                else:
                    root[par1] = par2
                    rank[par2] +=1
                    

        for p, c in edges:
            union(p, c)

        return find(source) ==  find(destination)

        

