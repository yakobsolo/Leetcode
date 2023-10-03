class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:

        graph = defaultdict(list)
        for s, e, c in roads:
            graph[s].append((e, c))
            graph[e].append((s, c))
        
        end  = n-1
        dist = {node: [inf, 0] for node in range(n)}
        q = []
        heappush(q, [0, 0])
        dist[0] = [0, 1]
        
        while q:
            cur_dst, cur_node = heappop(q)
            
            if cur_dst > dist[end][0]: break
                
            for child , time  in graph[cur_node]:
                temp = time+cur_dst
                if temp > dist[child][0]: continue
                elif temp == dist[child][0]:
                    dist[child][1] += dist[cur_node][1]
                else:
                    dist[child][0] = temp
                    dist[child][1] = dist[cur_node][1]
                    heappush(q, [temp, child])
        return dist[end][1]%((10**9)+7)
        