class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        finalPrice = [0]*n
        end = -1
        def path(node, p):
            if node == end:
                finalPrice[node] += price[node]
                return True
            
            for child in graph[node]:
                if child == p: continue
                if path(child, node):
                    finalPrice[node] += price[node]
                    return True
            return False
                    
                
        for s, e in trips:
            end = e
            path(s, -1)
            
        dp = {}
        def find(node, ok, p):
            if (node, ok) in dp: return dp[(node, ok)]
            take, leave = 0, 0
            if ok:
                take = finalPrice[node]//2
                
                for child in graph[node]:
                    if child == p: continue
                    take+=find(child, False, node)
                    
            for child in graph[node]:
                if child == p: continue
                leave+=find(child, True, node)
            
            dp[(node, ok)] = max(take, leave)
            return dp[(node, ok)]
                    
            
            
            
        
        ans = find(0, True, 0)
        return sum(finalPrice)-ans
        