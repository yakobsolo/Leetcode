class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        import collections
        graph= collections.defaultdict(list)
        
        r_len = len(routes)
        for b in range(r_len):
            for r in routes[b]:
                graph[r].append(b)
                
        
        q = collections.deque()
        q.append((source, 0))
        visted_stops = set()
        visted_stops.add(source)
        visted_bus = set()
        while q:
            
            stop , n = q.popleft()
            if stop == target: return n
            
            for bus in graph[stop]:
                if bus not in visted_bus:
                    for stops in routes[bus]:
                        if stops not in visted_stops:
                            q.append((stops, n+1))
                            visted_stops.add(stops)
                visted_bus.add(bus)
        return -1
            
        