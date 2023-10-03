class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for s, d, t in times:
            # print(s)
            graph[s].append((d, t))
            

            
        def dijkstra(graph, start):
            distances = {node: inf for node in range(1, n+1)}
            distances[start] = 0
            visited = set()
            q = [(0, start)]
            while q:
                cur_dis, cur_nod = heapq.heappop(q)
                
                if cur_nod in visited:
                    continue
                visited.add(cur_nod)
                for child, wht in graph[cur_nod]:
                    dis = cur_dis + wht
                    # print(distances, child)
                    if dis < distances[child]:
                        distances[child] = dis
                        heapq.heappush(q, (dis, child))
            return distances
        dis = dijkstra(graph, k)
        
        mx = 0
        for node in dis:
            if dis[node] == inf:
                return -1
            mx = max(mx, dis[node])
        return mx