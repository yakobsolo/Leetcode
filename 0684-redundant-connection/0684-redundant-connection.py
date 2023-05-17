class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        rep = [i for i in range(len(edges)+1)]
        rank = [1 for _ in range(len(edges)+1)]

        def find(node):
            if rep[node] == node:
                return node
            rep[node] = find(rep[node])
            return rep[node]
        
        
        def union(x, y):
            
            par1 = find(x)
            par2 = find(y)
            if par1 != par2:
                if rank[par1] > rank[par2]:
                    rep[par2] = par1
                    rank[par1] += 1
                else:
                    rep[par1] = par2
                    rank[par2] +=1
            else:
                return True
            return False

        for p, c in edges:
            if union(p, c): return [p, c]