class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        leng = len(roads)
        for r in range(leng):
            graph[roads[r][0]].append(roads[r][1])
            graph[roads[r][1]].append(roads[r][0])
        maxx = 0
        graph_copy = graph.copy()
        for key in graph:            
            leng_arr = len(graph[key])
            for i in range(n):
                if i not in graph[key] and i != key:
                    maxx = max(maxx, (leng_arr + len(graph_copy[i])))
                    
            for a in graph[key]:
                maxx = max(maxx, (leng_arr + len(graph_copy[a]) -1))
        return maxx
                