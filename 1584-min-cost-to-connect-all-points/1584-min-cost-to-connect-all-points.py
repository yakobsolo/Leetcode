class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        r_len = len(points)
        res = 0
        rep = {i:i for i in range(r_len)}
        rank = {i: 1 for i in range(r_len)}
        
        def find(n):
            if n == rep[n]: return n
            rep[n] = find(rep[n])
            return rep[n]
        
        def union(x, y):
            par1 = find(x)
            par2 = find(y)
            
            if par1!= par2:
                if rank[par1] <= rank[par2]:
                    rep[par2]  = par1
                    rank[par1] +=1
                else:
                    rep[par1] = par2
                    rank[par2] +=1
                return True
            
        connection = list()
        for i in range(r_len):
            for j in range(r_len):
                val = abs(points[i][0] - points[j][0]) + abs(points[j][1]- points[i][1])
                connection.append((val, i, j))
                
        connection.sort()
        for d, i, j in connection:
            if union(i, j):
                res +=d
        return res

        