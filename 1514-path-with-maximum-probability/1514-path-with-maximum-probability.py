class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        graph= defaultdict(list)
        i = 0
        for u, v in edges:
            graph[u].append([v, succProb[i]])
            graph[v].append([u , succProb[i]])
            i+=1
        
        heap = []
        dist = {node: 0 for node in range(n)}
        heappush(heap, [-1, start_node])
        
        visted=  set()
        
        while heap:
            
            cur_prob, cur_node = heappop(heap)
           
            
            if cur_node == end_node: return -cur_prob
            
            for child , succ in graph[cur_node]:
                
                prob  = succ*-cur_prob
                
                if prob>dist[child]: 
                    dist[child] = prob
                    heappush(heap, [-prob, child])
            
        return 0
        