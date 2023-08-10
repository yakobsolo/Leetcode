class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for s in stones:
            heappush(heap, -s)
        while len(heap)>1:
            y = heappop(heap)
            x = heappop(heap)
            if y<x : heappush(heap, -(-y+x))
        return -heap[0] if heap else 0
                