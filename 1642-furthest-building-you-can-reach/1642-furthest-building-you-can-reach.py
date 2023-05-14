class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        heap  = []
        import heapq
        for i in range(n-1):
            diff = heights[i+1] - heights[i]
            if diff>0:
                heapq.heappush(heap, diff)
                if len(heap) > ladders:
                    min_diff = heapq.heappop(heap)
                    bricks -= min_diff
                if bricks < 0: return i
        return n-1
            