class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        import heapq
        heap = []
        
        for pile in piles:
            heapq.heappush(heap, -pile)
        
        for i in range(k):
            top = heapq.heappop(heap)
            top = floor(top/2)
            heapq.heappush(heap, top)
        return -sum(heap)