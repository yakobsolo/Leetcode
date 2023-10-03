class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        import heapq
        
        graph = defaultdict(list)
        
        for f, t, w in flights:
            graph[f].append((t, w))
            
        def dijkastra(graph, start):
            distances  = {node: inf for node in range(n)} 
            heap = []
            heapq.heappush(heap, [0, start, k])
            distances[start] = 0
            visted = set()
            while heap:
                
                cur_dis,cur_node, cur_k = heapq.heappop(heap)
                # print(cur_node, cur_dis, cur_k)
                # print(distances)
                if cur_node == dst: return distances[dst]
                if (cur_node, cur_dis) in visted or cur_k == -1:
                    continue
                
                
                
                visted.add((cur_node, cur_dis))
                
                for child, wht in graph[cur_node]:
                    # print(cur_node, child)
                    temp = cur_dis+wht
                    if temp < distances[child]:
                        distances[child] = temp
                    
                    heapq.heappush(heap, [temp, child, cur_k-1])
                    
                    
            return -1
        return dijkastra(graph, src)
        
            
                
            