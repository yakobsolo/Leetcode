class Solution:
        
    
        
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        root = [i for i in range(n)]
        rank = [1 for _ in range(n)]

        def find(vert):
            if root[vert] == vert:
                return vert
            root[vert] = find(root[vert])
            return root[vert]

        def union(v1, v2):
            r1 = find(v1)
            r2 = find(v2)
            if r1 != r2:
                if rank[r1] > rank[r2]:
                    root[r2] = r1
                elif rank[r1] < rank[r2]:
                    root[r1] = r2
                else:
                    root[r2] = r1
                    rank[r1] += 1
       

        for e1, e2 in edges:
            union(e1, e2)

        root1 = find(source)
        root2 = find(destination)

        return root1 == root2


