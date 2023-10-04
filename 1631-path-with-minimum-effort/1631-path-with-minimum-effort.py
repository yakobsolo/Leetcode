class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        dire = {
            'up': (-1, 0),
            'down': (1, 0),
            'left': (0, -1),
            'right': (0, 1)
        }
        m = len(heights)
        n = len(heights[0])
        
        heap = [(0, (0,0))]
        visted = set()
        dist = [[float('inf') for i in range(n)] for j in range(m)]
        # print(dist)
        while heap:
            weight, node = heapq.heappop(heap)
            if node == (m-1, n-1):
                return weight
            visted.add((weight, node))
            
            # print(node, weight)
            for i in dire:
                x = node[0] + dire[i][0]
                y = node[1] + dire[i][1]
                if 0 <= x < m and 0 <= y < n:
                    tmp = max(weight, abs(heights[node[0]][node[1]] - heights[x][y]))
                    if (tmp, (x, y)) not in visted:
                        if tmp< dist[x][y]:
                            dist[x][y] = tmp
                            heappush(heap, (tmp, (x,y)))
                
                